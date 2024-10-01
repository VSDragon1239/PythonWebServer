MainFolder = 'FileManager/'
pagesFolder = MainFolder + 'pages/'
staticFolder = MainFolder + 'static/'
dataFolder = MainFolder + 'data/'
typeFile = '.html'
typeData = '.json'
mainPage = pagesFolder + 'mainPage' + typeFile
aboutPage = pagesFolder + 'aboutPage' + typeFile
authPage = pagesFolder + 'authPage' + typeFile


imageFolder = staticFolder + 'images/'
jsFolder = staticFolder + 'js/'
cssFolder = staticFolder + 'css/'

# 0 - заглушка чтобы нумерация начиналась с [1, 2, ..., n]
ArrayPages = [0, mainPage, aboutPage, authPage]


ArrayPaths = [0, '/', [0, '/about', '/about/'], [0, '/log', '/reg', '/auth']]
