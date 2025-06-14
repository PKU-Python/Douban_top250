# 豆瓣电影 Top250 爬虫项目

## 项目目标
爬取 [豆瓣电影 Top250](https://movie.douban.com/top250) 的电影信息。

## 实现要求
1. 使用 Python 实现
2. 模拟分页访问，5~20s 进行一次分页请求
3. 对电影信息的元数据进行格式化，输出到 CSV 文件中

## 输出格式
电影信息将按以下结构输出：

- 电影名称：肖申克的救赎
- 别称：The Shawshank Redemption / 月黑高飞(港) / 刺激1995(台)
- 导演：陈凯歌 Kaige Chen
- 主演：张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...
- 年代：1993
- 地区：中国大陆 中国香港
- 影片类型：剧情 爱情 同性
- 评分：9.7
- 评价人数：2345163人评价
- 简介：风华绝代

## 原始数据示例
以下是网页中的原始数据格式示例：

```html
<div class="info">
    <div class="hd">
        <a href="https://movie.douban.com/subject/1291546/">
            <span class="title">霸王别姬</span>
            <span class="other">&nbsp;/&nbsp;再见，我的妾  /  Farewell My Concubine</span>
        </a>
        <span class="playable">[可播放]</span>
    </div>
    <div class="bd">
        <p>
            导演: 陈凯歌 Kaige Chen&nbsp;&nbsp;&nbsp;主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...<br>
            1993&nbsp;/&nbsp;中国大陆 中国香港&nbsp;/&nbsp;剧情 爱情 同性
        </p>
        
        <div>
            <span class="rating5-t"></span>
            <span class="rating_num" property="v:average">9.6</span>
            <span property="v:best" content="10.0"></span>
            <span>2345163人评价</span>
        </div>

        <p class="quote">
            <span>风华绝代。</span>
        </p>
    </div>
</div>