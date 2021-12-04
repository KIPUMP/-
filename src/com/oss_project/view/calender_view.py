from tkcalendar import Calendar
from tkinter import Tk
#-----------------------------------------------------------calender----------------------------------------------------------
class MyCalendar(Calendar):
    def _next_month(self):
        Calendar._next_month(self)
        self.event_generate('<<CalendarMonthChanged>>')
    def _prev_month(self):
        Calendar._prev_month(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _next_year(self):
        Calendar._next_year(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _prev_year(self):
        Calendar._prev_year(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def get_displayed_month_year(self):
        return self._date.month, self._date.year
        
    def on_change_month(event):
        Calendar.calevent_remove('all')
        year, month = Calendar.get_displayed_month_year()
        print(year, month)

#calender 버튼 리스너
def clickcalender():
    w = Tk()
    w.title("calendar")
    cal = MyCalendar(w)
    cal.pack()
    cal.bind('<<CalendarMonthChanged>>')
    w.mainloop()