https://movie.douban.com/top250

爬取上述网址 豆瓣电影 top250 的电影信息，要求：

使用Python实现；
模拟分页访问，5~20s 进行一次分页请求；
对于电影信息的元数据进行格式化，输出到csv 文件中；


结构化输出内容如下：

电影名称：肖申克的救赎
别称：The Shawshank Redemption  / 月黑高飞(港) / 刺激1995(台) 
导演：陈凯歌 Kaige Chen
主演：张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...
年代：1993
地区：中国大陆 中国香港
影片类型：剧情 爱情 同性
评分：9.7
评价人数：2345163人评价
简介：风华绝代。


对应的原始网页数据如下：
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
                            

    <p>
        
        <span class="gact">
            <a href="https://movie.douban.com/wish/76765279/update?add=1291546" target="_blank" class="j a_collect_btn" name="sbtn-1291546-wish" rel="nofollow">想看</a>
        </span>&nbsp;&nbsp;
        
        <span class="gact">
            <a href="https://movie.douban.com/collection/76765279/update?add=1291546" target="_blank" class="j a_collect_btn" name="sbtn-1291546-collection" rel="nofollow">看过</a>
        </span>&nbsp;&nbsp;
    </p>

                    </div>
                </div>