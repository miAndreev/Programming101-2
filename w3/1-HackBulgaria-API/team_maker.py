import requests
import json
import random

class Team_Maker():
    def __init__(self):
        self.data = {}
        self.courses = []
        self.teams = []

    def main():

        data = get_json_from_file("1.txt") 
        courses = []
        print(data[0]["courses"])
        for s in data:
            for c in s["courses"]:
               if c["name"] not in courses:
                    courses.append(c["name"])
        
        print (courses)
        for i in range(0,len(courses)):
            print ("[" + str(i) + "] " + courses[i] )
        match_teams(data, courses, 0, 2, 1)

    def get_json_from_api(self):
        r = requests.get("https://hackbulgaria.com/api/students/")
        self.data = r.json()
        r.close()
        return data

    def get_json_from_file(self, file_name):
        f = open(file_name,"r")
        dump = f.read()
        f.close()
        self.data = json.loads(dump)
        return self.data

    def list_all_courses(self):
        courses = []
        for s in self.data:
            for c in s["courses"]:
                if c["name"] not in courses:
                    courses.append(c["name"])
        self.courses = courses
        return courses

    def print_all_courses(self):
        for i in range(0,len(self.courses)):
            print ("[" + str(i) + "] " + self.courses[i] )

    def interface(self):
        courses = []
        help_str = """Hello, you can use one the the following commands:\n
                list_courses - this lists all the courses that are available now.\n
                match_teams <course_id>, <team_size>, <group_time>\n
                """
        print (help_str)
        exit_command = False
        while not exit_command:
            commands = raw_input()
            commands = commands.split()
            courses = []
            data = get_json()        
            if commands[0] == "list_courses":

                courses = list_all_courses(data)
            elif commands[0] == "match_teams":
                course_id = commands[1]
                team_size = commands[2]
                group_time = commands[3]
                teams = match_teams(data, courses, course_id, team_size, group_time)

                for group in teams:
                    print ("==========")
                    for s in group:
                        print (s["name"])

            elif commands[0] == "exit_command" :
                exit_command = True

    def match_teams(self, course_id, team_size, group_time):
        students = []
        for s in self.data:
            for c in s["courses"]:
                if c["name"] == self.courses[course_id]:
                    if c["group"] == group_time:
                        students.append(s)

        #arrange random and cut
        #for s in students:
        #    print (s["name"])
        sr = random.shuffle(students)
        #print("---")
        #for s in students:
        #    print (s["name"])

        teams = []
        number_of_teams = len(students)/team_size
        if int(number_of_teams)*10 != int(number_of_teams*10):
            number_of_teams = int(number_of_teams) + 1
        current_start_index = 0
        for i in range(1,number_of_teams):
            teams.append(students[current_start_index:current_start_index + team_size])
            current_start_index = current_start_index + team_size

        #print (teams) 
        self.teams = teams 
        return teams

if __name__ == '__main__':
    #test()
    interface()