from itertools import islice
from tkinter import *

def nth_index(iterable, value, n):
  matches = (idx for idx, val in enumerate(iterable) if val == value)
  return next(islice(matches, n - 1, n), None)

class Course:
  instances = []

  def __init__(self, code, name, classroom, instructor, day, start_time,
               end_time):
    self.name = name
    self.code = code
    self.classroom = classroom
    self.instructor = instructor
    self.day = day
    self.start_time = start_time
    self.end_time = end_time
    self.__class__.instances.append(self)

class Schedule:
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
  programme = [[
    " 8.30 -  9.30", " 9.30 - 10.30", "10.30 - 11.30", "11.30 - 12.30",
    "12.30 - 13.30", "13.30 - 14.30", "14.30 - 15.30", "15.30 - 16.30",
    "16.30 - 17.30"
  ],
  [
    " 8.30 -  9.30", " 9.30 - 10.30", "10.30 - 11.30",
    "11.30 - 12.30", "12.30 - 13.30", "13.30 - 14.30",
    "14.30 - 15.30", "15.30 - 16.30", "16.30 - 17.30"
  ],
  [
    " 8.30 -  9.30", " 9.30 - 10.30", "10.30 - 11.30",
    "11.30 - 12.30", "12.30 - 13.30", "13.30 - 14.30",
    "14.30 - 15.30", "15.30 - 16.30", "16.30 - 17.30"
  ],
  [
    " 8.30 -  9.30", " 9.30 - 10.30", "10.30 - 11.30",
    "11.30 - 12.30", "12.30 - 13.30", "13.30 - 14.30",
    "14.30 - 15.30", "15.30 - 16.30", "16.30 - 17.30"
  ],
  [
    " 8.30 -  9.30", " 9.30 - 10.30", "10.30 - 11.30",
    "11.30 - 12.30", "12.30 - 13.30", "13.30 - 14.30",
    "14.30 - 15.30", "15.30 - 16.30", "16.30 - 17.30"
  ]]

  def __init__(self):
    self.courses = []

  def add_course(self, course):
    self.courses.append(course)

  def print_schedule(self):
    collusion = False
    allDays = [i.day for i in Course.instances]
    starts = [k.start_time for k in Course.instances]
    ends = [k.end_time for k in Course.instances]
    collapsingDays = []
    
    for day in set(allDays):
      allHours = []
      count = allDays.count(day)
      
      if count == 1:
        continue
      else:
        allHours = []
        collapsingDayIndex = [x for x, n in enumerate(allDays) if n == day]
        
        for i in collapsingDayIndex:
          
          for hours in range(starts[i], ends[i]):
            
            allHours.append(hours)
            
      if len(allHours) != len(set(allHours)):
        collapsingDays.append(day)
        collusion = True
      else:
        continue
        
    if collusion:
      collapsingDays.sort()
      a = ", ".join(collapsingDays)
      print(
        f"There are some courses which are collapsing on {a}, please rewrite the courses."
      )
      return 0

    for course in self.courses:
      for j in range(course.start_time - 9, course.end_time - 9):
        Schedule.programme[Schedule.days.index(course.day)][j] += f"      {course.code} {course.name} class from {course.instructor} at {course.classroom}"
    for i in range(len(Schedule.days)):
      print(Schedule.days[i], ":")
      for k in Schedule.programme[i]:
        print(k)
        pass

  def print_table(self, root):
    collusion = False
    allDays = [i.day for i in Course.instances]
    starts = [k.start_time for k in Course.instances]
    ends = [k.end_time for k in Course.instances]
    for day in set(allDays):
      allHours = []
      count = allDays.count(day)
      if count == 1:
        continue
      else:
        allHours = []
        collapsingDayIndex = [x for x, n in enumerate(allDays) if n == day]
        for i in collapsingDayIndex:
          for hours in range(starts[i], ends[i]):
            allHours.append(hours)
      if len(allHours) != len(set(allHours)):
        collusion = True
      else:
        continue
    if collusion:
      return 0

    week = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [0, 1, 2, 3, 4, 5, 6, 7, 8]]
    
    for course in self.courses:
      for i in range(course.start_time - 9, course.end_time - 9):
        self.e = Entry(root, width=20, fg='#181a1f', font=('Arial', 12))
        self.e.grid(row=i, column=Schedule.days.index(course.day))
        self.e.insert(END, course.code)
        week[Schedule.days.index(course.day)].remove(i)

    for i in range(5):
      for hour in week[i]:
        self.e = Entry(root, width=20, fg='#181a1f', font=('Arial', 12))
        self.e.grid(row=hour, column=i)
        self.e.insert(END, "")


schedule = Schedule()
schedule.add_course(
  Course("EEF 211E", "Basics of Electrical Circuits", "EEB 5102",
         "Metin Hüner", "Monday", 9, 12))
schedule.add_course(
  Course("MAT 202E", "Numerical Methods", "EEB 5304", "Emine Ayaz", "Monday",
         13, 16))
schedule.add_course(
  Course("EEF 271E", "Probability and Statistics", "MED A36", "Mustafa Doğan",
         "Tuesday", 9, 12))
schedule.add_course(
  Course("ING 201A", "Academic Writing", "Home", "Gamze Avcı", "Tuesday", 14,
         16))
schedule.add_course(
  Course("ELK 107E", "Introduction to Python", "Home", "Ali Sinan Çabuk",
         "Wednesday", 9, 13))
schedule.add_course(
  Course("EEF 210E", "Differential Equations", "INB A105", "Kamil Karaçuha",
         "Thursday", 13, 16))
schedule.add_course(
  Course("EEF 205E", "Logic Design", "KIM D102", "Osman Kaan Erol", "Friday",
         9, 12))

schedule.print_schedule()
root = Tk()
schedule.print_table(root)
root.mainloop()
