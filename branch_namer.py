#!/usr/bin/env python3
"""Suggest branch names from issue titles"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Suggest branch names from issue titles")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("branch-namer v0.1.0");return
 print(f"[12:01] branch-namer ready")
if __name__=="__main__":main()
