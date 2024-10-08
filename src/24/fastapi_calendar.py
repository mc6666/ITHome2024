from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
from dataclasses import dataclass
from datetime import datetime

app = FastAPI(debug=True, redirect_slashes=False)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@dataclass
class Event():
    # id: int
    text: str
    start:datetime
    end:datetime 
    
def execute_SQL(sql):
    con = sqlite3.connect("calendar.db")
    cur = con.cursor()
    result = cur.execute(sql)
    con.commit() 
    con.close()
    return result

def execute_select_SQL(sql):
    con = sqlite3.connect("calendar.db")
    cur = con.cursor()
    result = cur.execute(sql)
    data = result.fetchall()
    con.commit() 
    con.close()
    return data

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )
    
@app.get("/api/CalendarEvents")
async def get_events(start, end):
    sql = f"select * from calendar where start >= '{start}' and end <= '{end}'"
    response = []
    result = execute_select_SQL(sql)
    for row in result:
        dict1 = {}
        dict1['id'] = row[0]
        dict1['text'] = row[1]
        dict1['start'] = row[2]
        dict1['end'] = row[3]
        response.append(dict1)
    return response  
    
@app.post("/api/CalendarEvents")
async def add_events(event:Event):
    # SSprint(event.start, event.end, event.text)
    sql = f"insert into calendar (text, start, end) values ('{event.text}', '{event.start}', '{event.end}')"
    result = execute_select_SQL(sql)
    dict1 = {}
    dict1['id'] = result
    dict1['text'] = event.text
    dict1['start'] = event.start
    dict1['end'] = event.end
    return dict1
    
@app.put("/api/CalendarEvents/{id}")
async def update_events(id, event:Event):
    # print(event.start, event.end, event.text)
    sql = f"update calendar set text='{event.text}', start='{event.start}', end='{event.end}' "
    sql += f" where id={id}"
    result = execute_SQL(sql)
    return {}
    
@app.delete("/api/CalendarEvents/{id}")
async def delete_events(id):
    sql = f"delete from calendar where id = {id}"
    result = execute_SQL(sql)
    return {}    