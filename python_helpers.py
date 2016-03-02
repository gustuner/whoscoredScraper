# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 10:40:03 2016

@author: Jonathan Klaiber
"""

from file_helpers import open_from_disk
from file_helpers import write_to_disk

def sync_lists(listname1, listname2):          
    syncDays = open_from_disk(listname1)
    syncMatchday = open_from_disk(listname2)
    
    comparison = []
    for syncentry in syncMatchday:
        comparison.append(syncentry.split('-')[1])
    mismatch = [x for x in syncDays if x not in list(comparison)]
    
    print '\n' + str(len(mismatch)) + ' values will be removed from '+ listname1 + '.\n'
    print 'Sync completed.\n'
    for val in mismatch:
        syncDays.remove(val)
    write_to_disk(syncDays, listname1)

def split_list(splitlist, nparts):
    returnList = []
    for i in xrange(0, len(splitlist), nparts):
        returnList.append(splitlist[i:i + nparts])
    return returnList

def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result