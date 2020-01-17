include_directories(../inc /usr/local/include)
aux_source_directory(./ Test)
add_library(test_zoo ${Test})