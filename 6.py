#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  6.py
#  

import zipfile, re, itertools

comments = []

file_list  = zipfile.ZipFile('channel.zip', 'r')

print(len(file_list.namelist()))

next_str = str(90052)

def next_file(next_str):
	for r in range(908):	
		text_str = str(file_list.read(next_str+'.txt'))
		next_str = "".join(re.findall('\d+', text_str))
		comments.append(file_list.getinfo(next_str+'.txt').comment)
	return next_str


print(next_file(next_str))
comment_set = set(re.findall('[a-z]|[A-Z]', str(comments)))
print(list(itertools.combinations(comment_set, 6)))

print('Close enough')




