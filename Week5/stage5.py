# 인터넷에서 이미지를 가져오기 위한 방법 urlretrieve

from urllib.request import urlretrieve

src = "https://movie-phinf.pstatic.net/20200428_196/1588038709486FYyHu_JPEG/movie_image.jpg?type=m203_290_2"
urlretrieve(src, "poster.png")