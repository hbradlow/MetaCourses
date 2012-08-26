import requests
from bs4 import BeautifulSoup
from courses.models import Course, School, Category, Material
import json

def edx(debug=False):
    base_url = "https://www.edx.org"
    r = requests.get(base_url + "/courses")
    soup = BeautifulSoup(r.text)

    for column in soup("section", {"class":"university-column"}):
        for course in column("article",{"class":"course"}):
            course_id = "/".join(course['id'].split("/")[:-1])
            school_name = course['id'].split("/")[0][:-1].lower()
            try:
                school = School.objects.filter(name__icontains=school_name)[0]
            except:
                school = School.objects.create(name=school_name)
            try:
                m = Course.objects.filter(type="edx").filter(course_id=course_id)[0]
            except:
                m = Course()

            material_names = ["Assignments and solutions","Projects and examples","Multimedia content","Exams and solutions"]
            materials = []
            for name in material_names:
                try:
                    material = Material.objects.get(name=name)
                except:
                    material = Material.objects.create(name=name)
                materials.append(material)

            m.title = " ".join(course("header")[0]("h2")[0].get_text().split(" ")[1:])
            m.link = base_url + course("a")[0]['href']
            m.image_url = base_url + course("img")[0]['src']
            m.type = "edx"
            m.course_id = course_id
            m.school = school
            m.save()

            m.materials = materials
            m.save()

            if debug:
                print m

def coursera(debug=False):
    r = requests.get("https://www.coursera.org/maestro/api/topic/list?full=1")
    data = json.loads(r.text)

    for course in data:
        course_id = course['id']
        school_name = course['universities'][0]['name'].lower()
        category_names = [a['name'].lower() for a in course['categories']]
        categories = []
        try:
            school = School.objects.filter(name__icontains=school_name)[0]
        except:
            school = School.objects.create(name=school_name)
        for category_name in category_names:
            try:
                category = Category.objects.get(name=category_name)
            except:
                category = Category.objects.create(name=category_name)
            categories.append(category)
        try:
            m = Course.objects.filter(type="coursera").filter(course_id=course_id)[0]
        except:
            m = Course()

        material_names = ["Assignments and solutions","Projects and examples","Multimedia content","Exams and solutions"]
        materials = []
        for name in material_names:
            try:
                material = Material.objects.get(name=name)
            except:
                material = Material.objects.create(name=name)
            materials.append(material)

        m.title = course['name']
        m.link = course['social_link']
        m.image_url = course['small_icon']
        m.course_id = course_id
        m.type = "coursera"
        m.school = school
        m.save()
        m.categories = categories
        m.materials = materials 
        m.save()

        if debug:
            print m

def mit(debug=False):
    base_url = "http://ocw.mit.edu"
    r = requests.get(base_url + "/courses/")
    soup = BeautifulSoup(r.text)

    for course_list in soup("div",{"class":"course_list"}):
        category_name = str(course_list("div",{"class":"table_head"})[0]("a")[0].string).lower()
        for row in course_list("tr",{"class":"row"}) + course_list("tr",{"class":"alt-row"}):
            course_id = row("td")[2].string
            school_name = "mit"
            try:
                school = School.objects.filter(name__icontains=school_name)[0]
            except:
                school = School.objects.create(name=school_name)

            try:
                category = Category.objects.get(name=category_name)
            except:
                category = Category.objects.create(name=category_name)

            try:
                m = Course.objects.filter(type="mit").filter(course_id=str(course_id))[0]
            except:
                m = Course()
                
            material_names = [a['alt'] for a in row("td")[1]("a")]
            materials = []
            for name in material_names:
                try:
                    material = Material.objects.get(name=name)
                except:
                    material = Material.objects.create(name=name)
                materials.append(material)

            m.title = row("td")[3]("a")[0]("u")[0].string
            m.link = base_url + row("td")[3]("a")[0]['href']
            m.type = "mit"
            m.course_id = course_id
            m.school = school

            m.save()
            m.categories = [category]
            m.materials = materials
            m.save()

            if debug:
                print m

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]
def gather_mit_images(courses,chunk_size=50):
    import grequests
    import math
    base_url = "http://ocw.mit.edu"
    course_chunks = chunks(courses,chunk_size)
    num_chunks = int(math.ceil(len(courses)/float(chunk_size)))
    num = 1
    for chunk in course_chunks:
        urls = [course.link for course in chunk]
        rs = (grequests.get(u) for u in urls)
        results = grequests.map(rs)
        for course,result in zip(chunk,results):
            soup = BeautifulSoup(result.text)
            src = soup("img",{"id":"chp_image"})[0]['src']
            course.image_url = base_url + src
            course.save()
            print course.image_url
        print "Finished chunk " + str(num) + " out of " + str(num_chunks)
        num += 1
                
def scrape_all(debug=False):
    coursera(debug)
    edx(debug)
    mit(debug)
