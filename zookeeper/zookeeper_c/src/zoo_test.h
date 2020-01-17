#pragma once
#include "common.h" 
#include "zookeeper.h"
#include "zookeeper_log.h"
#include <unistd.h>
using namespace std;
int TestMain();
void create(zhandle_t *zkhandle,char *str);
