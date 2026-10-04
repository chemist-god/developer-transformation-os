#!/usr/bin/env python3
"""
21-Day Developer Transformation Program - Local Tracker
Tracks metrics, reading page proofs, speaking drills, and scores.
"""

import json
import os
import sys
from datetime import datetime

DATA_FILE = "progress.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "current_day": 1,
            "streak": 0,
            "baseline": {},
            "logs": {}
        }
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def status():
    data = load_data()
    day = data["current_day"]
    print("\n" + "=" * 72)
    print(f"  DEVELOPER TRANSFORMATION OS | DAY {day:02d} OF 21")
    print(f"  Current Streak: {data.get('streak', 0)} days | Total Days Logged: {len(data['logs'])}")
    print("=" * 72)
    
    if str(day) in data["logs"]:
        log = data["logs"][str(day)]
        print(f"Status for Day {day}: [COMPLETED]")
        print(f"  * Deep Work:     {log.get('deep_work_minutes', 0)} mins")
        print(f"  * Reading:       {log.get('pages_read', 0)} pages ({log.get('book_title', 'N/A')})")
        print(f"  * Filler Words:  {log.get('filler_words', 0)}")
        print(f"  * Scores:        Comm: {log.get('comm_score')}/5 | Tech: {log.get('tech_score')}/5 | Disc: {log.get('disc_score')}/5")
    else:
        print(f"Status for Day {day}: [PENDING EVENING DEBRIEF]")
        print("  Run: python tracker.py log (when ready to complete your day)")
    print("=" * 72 + "\n")

def log_day():
    data = load_data()
    day = data["current_day"]
    print("\n" + "=" * 72)
    print(f"  LOGGING EVENING DEBRIEF: DAY {day:02d}")
    print("=" * 72)
    
    print("\n--- 1. READING & CONCEPT PROOF ---")
    book = input("Book title: ").strip()
    pages = int(input("Total pages read today: ") or "0")
    concept = input("Key concept learned (active retrieval check): ").strip()
    
    print("\n--- 2. EXECUTION & DRILLS ---")
    deep_work = int(input("Deep work minutes completed (target 90): ") or "0")
    speaking_rec = input("Link/filename of speaking recording: ").strip()
    filler_words = int(input("Filler words counted in recording: ") or "0")
    git_commit = input("Git commit hash of technical exercise: ").strip()
    
    print("\n--- 3. BEHAVIORAL SCORES (1=Novice, 3=Proficient, 5=Mastery) ---")
    comm = int(input("  Communication & Speaking Score (1-5): ") or "3")
    tech = int(input("  Technical & Architecture Score (1-5): ") or "3")
    disc = int(input("  Discipline & Focus Score (1-5): ") or "3")
    
    print("\n--- 4. DAILY ACCOUNTABILITY REFLECTION ---")
    reflection = input("What friction or hesitation did you overcome today?: ").strip()
    
    data["logs"][str(day)] = {
        "timestamp": datetime.now().isoformat(),
        "book_title": book,
        "pages_read": pages,
        "concept": concept,
        "deep_work_minutes": deep_work,
        "speaking_recording": speaking_rec,
        "filler_words": filler_words,
        "git_commit": git_commit,
        "comm_score": comm,
        "tech_score": tech,
        "disc_score": disc,
        "reflection": reflection
    }
    
    data["streak"] = data.get("streak", 0) + 1
    if day < 21:
        data["current_day"] = day + 1
        
    save_data(data)
    print(f"\n[+] Day {day} successfully logged. Current day is now Day {data['current_day']}.\n")

def report():
    data = load_data()
    print("\n" + "=" * 72)
    print("  TRANSFORMATION PROGRESS REPORT")
    print("=" * 72)
    if not data["logs"]:
        print("  No days logged yet. Start Day 1 to build your data.")
        print("=" * 72 + "\n")
        return

    print(f"{'Day':<6} {'Pages':<8} {'DeepWork':<10} {'Fillers':<10} {'Comm':<6} {'Tech':<6} {'Disc':<6}")
    print("-" * 72)
    for d in sorted([int(k) for k in data["logs"].keys()]):
        e = data["logs"][str(d)]
        print(f"{d:<6} {e.get('pages_read', 0):<8} {e.get('deep_work_minutes', 0):<10} "
              f"{e.get('filler_words', 0):<10} {e.get('comm_score', 0):<6} "
              f"{e.get('tech_score', 0):<6} {e.get('disc_score', 0):<6}")
    print("=" * 72 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "log":
        log_day()
    elif len(sys.argv) > 1 and sys.argv[1] == "report":
        report()
    else:
        status()