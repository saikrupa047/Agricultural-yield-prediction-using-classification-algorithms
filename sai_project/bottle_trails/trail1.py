import pickle

random_forest  = pickle.load(open('./public/static/reg.sav','rb'))
state_dict = {'Washington': 1, 'Oklahoma': 2, 'Kansas': 3, 'Texas': 4, 'Montana': 5}
mid=32.9
county_dict = {'Adams': 1, 'Alfalfa': 2, 'Allen': 3, 'Anderson': 4, 'Archer': 5, 'Armstrong': 6, 'Atascosa': 7, 'Atchison': 8, 'Bailey': 9, 'Barton': 10, 'Beaver': 11, 'Beckham': 12, 'Bell': 13, 'Bexar': 14, 'Big Horn': 15, 'Blaine': 16, 'Bosque': 17, 'Bourbon': 18, 'Bowie': 19, 'Briscoe': 20, 'Broadwater': 21, 'Brown': 22, 'Bryan': 23, 'Butler': 24, 'Caddo': 25, 'Callahan': 26, 'Canadian': 27, 'Carbon': 28, 'Carson': 29, 'Carter': 30, 'Cascade': 31, 'Castro': 32, 'Chase': 33, 'Chautauqua': 34, 'Cherokee': 35, 'Cheyenne': 36, 'Childress': 37, 'Chouteau': 38, 'Cimarron': 39, 'Clark': 40, 'Clay': 41, 'Cleveland': 42, 'Cochran': 43, 'Coffey': 44, 'Coke': 45, 'Coleman': 46, 'Collin': 47, 'Collingsworth': 48, 'Columbia': 49, 'Comanche': 50, 'Concho': 51, 'Cooke': 52, 'Coryell': 53, 'Cottle': 54, 'Cotton': 55, 'Cowley': 56, 'Craig': 57, 'Custer': 58, 'Dallam': 59, 'Dallas': 60, 'Daniels': 61, 'Deaf Smith': 62, 'Decatur': 63, 'Delta': 64, 'Denton': 65, 'Dewey': 66, 'Dickens': 67, 'Dickinson': 68, 'Donley': 69, 'Douglas': 70, 'Eastland': 71, 'Edwards': 72, 'Ellis': 73, 'Ellsworth': 74, 'Falls': 75, 'Fannin': 76, 'Fergus': 77, 'Finney': 78, 'Flathead': 79, 'Floyd': 80, 'Foard': 81, 'Ford': 82, 'Franklin': 83, 'Frio': 84, 'Gallatin': 85, 'Garfield': 86, 'Garvin': 87, 'Geary': 88, 'Gillespie': 89, 'Glacier': 90, 'Gove': 91, 'Grady': 92, 'Grant': 93, 'Gray': 94, 'Grayson': 95, 'Greeley': 96, 'Greenwood': 97, 'Greer': 98, 'Guadalupe': 99, 'Hamilton': 100, 'Hansford': 101, 'Hardeman': 102, 'Harmon': 103, 'Harper': 104, 'Harvey': 105, 'Haskell': 106, 'Hemphill': 107, 'Hill': 108, 'Hunt': 109, 'Hutchinson': 110, 'Jack': 111, 'Jackson': 112, 'Jefferson': 113, 'Jewell': 114, 'Johnson': 115, 'Jones': 116, 'Judith Basin': 117, 'Karnes': 118, 'Kaufman': 119, 'Kay': 120, 'Kent': 121, 'Kingfisher': 122, 'Kingman': 123, 'Kiowa': 124, 'Kleberg': 125, 'Klickitat': 126, 'Knox': 127, 'Labette': 128, 'Lake': 129, 'Lamb': 130, 'Lampasas': 131, 'Lane': 132, 'Leavenworth': 133, 'Liberty': 134, 'Limestone': 135, 'Lincoln': 136, 'Linn': 137, 'Lipscomb': 138, 'Logan': 139, 'Lubbock': 140, 'Lynn': 141, 'Lyon': 142, 'Major': 143, 'Marion': 144, 'Mayes': 145, 'McClain': 146, 'McCone': 147, 'McCulloch': 148, 'McLennan': 149, 'McPherson': 150, 'Meade': 151, 'Medina': 152, 'Menard': 153, 'Miami': 154, 'Love': 155, 'Lamar': 156}

svm = pickle.load(open('./public/static/class.sav','rb'))


from bottle import Bottle , RouteError, request, run,route,template,static_file

@route('/')
def index():
    return template('index_sai.html')

@route('/static/<file>')
def show(file):
    return static_file(file , root='./public/static/')

@route('/login',method='POST')
def process():
    state = request.forms.get('state')
    county = request.forms.get('county')
    cloudcover = request.forms.get('cloudcover')
    duepoint = request.forms.get('duepoint')
    humidity = request.forms.get('humidity')
    pressure = request.forms.get('pressure')
    tempmin = request.forms.get('tempmin')
    tempmax = request.forms.get('tempmax')
    windspeed = request.forms.get('windspeed')
    lis = [state,county,cloudcover,duepoint,humidity,pressure,tempmin,tempmax,windspeed]
    print(lis)
    a = ''
    if None not in lis :
        if a not in lis:
            s_val = state_dict[state]
            c_val = county_dict[county]
            lis[0] = s_val
            lis[1] = c_val
            res = random_forest.predict([lis])
            if mid>=res[0]:
                res2 = 'low'
            else:
                res2 = 'high'
    else:
        res = None
        res2 = None
    return template('from_sai.html',res=res,high=res2)

run(debug=True,reloader=True ,host='localhost', port=8080) 