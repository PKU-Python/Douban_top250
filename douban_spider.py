import requests
from bs4 import BeautifulSoup
import time
import random
import logging
import csv
import re
import os

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DoubanSpider:
    def __init__(self):
        self.base_url = "https://movie.douban.com/top250"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.movies = []

    def get_page(self, page):
        """获取指定页面的内容"""
        url = f"{self.base_url}?start={(page-1)*25}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logging.error(f"获取页面 {page} 失败: {str(e)}")
            return None

    def parse_page(self, html):
        """解析页面内容"""
        if not html:
            return []
        
        soup = BeautifulSoup(html, 'html.parser')
        movie_items = soup.select('.grid_view li')
        
        page_movies = []
        for item in movie_items:
            try:
                # 电影名称
                title_tag = item.select_one('.title')
                title = title_tag.text if title_tag else ''
                if not title_tag:
                    logging.warning('缺失电影名称')
                
                # 别称
                other_tag = item.select_one('.other')
                other = other_tag.text.strip() if other_tag else ''
                if not other_tag:
                    logging.warning('缺失别称')
                
                # 导演、主演、年代、地区、影片类型
                bd_p_tag = item.select_one('.bd p')
                director = ''
                actors = ''
                year = ''
                region = ''
                genre = ''
                if bd_p_tag:
                    bd_text = bd_p_tag.text.strip()
                    logging.debug(f"bd_p_tag原始文本: {bd_text}")
                    bd_lines = bd_text.split('\n')
                    for i, line in enumerate(bd_lines):
                        logging.debug(f"bd_p_tag第{i+1}行: {line}")
                    if len(bd_lines) >= 1:
                        first_line = bd_lines[0].strip()
                        director_match = re.search(r'导演: ([^\\s]+)', first_line)
                        if director_match:
                            director = director_match.group(1)
                        actors_match = re.search(r'主演: ([^\\s]+)', first_line)
                        if actors_match:
                            actors = actors_match.group(1)
                    if len(bd_lines) >= 2:
                        second_line = bd_lines[1].strip()
                        year_match = re.search(r'(\\d{4})', second_line)
                        if year_match:
                            year = year_match.group(1)
                        region_match = re.search(r'([^/]+)/', second_line)
                        if region_match:
                            region = region_match.group(1).strip()
                        genre_match = re.search(r'/([^/]+)$', second_line)
                        if genre_match:
                            genre = genre_match.group(1).strip()
                else:
                    logging.warning('缺失bd p信息')
                
                # 评分
                rating_tag = item.select_one('.rating_num')
                rating = rating_tag.text if rating_tag else ''
                if not rating_tag:
                    logging.warning('缺失评分')
                
                # 评价人数
                people_tag = item.select_one('.rating_num + span')
                people = people_tag.text.strip('(').strip('人评价)') if people_tag else ''
                if not people_tag:
                    logging.warning('缺失评价人数')
                
                # 简介
                quote_tag = item.select_one('.quote .inq')
                quote = quote_tag.text if quote_tag else ''
                if not quote_tag:
                    logging.debug('无简介')
                
                movie = {
                    '电影名称': title,
                    '别称': other,
                    '导演': director,
                    '主演': actors,
                    '年代': year,
                    '地区': region,
                    '影片类型': genre,
                    '评分': rating,
                    '评价人数': people,
                    '简介': quote,
                }
                page_movies.append(movie)
            except Exception as e:
                logging.error(f"解析电影信息失败: {str(e)}")
                continue
        
        return page_movies

    def save_to_csv(self, filename='douban_top250.csv'):
        """保存数据到CSV文件"""
        if not self.movies:
            logging.warning("没有数据可保存")
            return

        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, filename)
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, fieldnames=self.movies[0].keys())
                writer.writeheader()
                writer.writerows(self.movies)
            logging.info(f"数据已保存到 {file_path}")
        except Exception as e:
            logging.error(f"保存CSV文件失败: {str(e)}")

    def run(self):
        """运行爬虫"""
        for page in range(1, 11):
            logging.info(f"正在爬取第 {page} 页")
            html = self.get_page(page)
            movies = self.parse_page(html)
            self.movies.extend(movies)
            
            # 随机等待5-20秒
            wait_time = random.uniform(5, 20)
            logging.info(f"等待 {wait_time:.2f} 秒后继续...")
            time.sleep(wait_time)

        # 保存数据到CSV
        self.save_to_csv()

if __name__ == "__main__":
    spider = DoubanSpider()
    spider.run() 