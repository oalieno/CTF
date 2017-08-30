# import idc
# import idaapi

syms = ['atoi', 'atol', 'isascii', 'isblank', 'isalpha', 'isdigit', 'isalnum', 'isspace', 'isupper', 'islower', 'tolower', 'toupper', 'isprint', 'ispunct', 'tzset', 'tp2tm', 'localtime', 'gmtime', 'mktime', 'pre_main', 'malloc', 'free', 'memtst_full', 'memtst_show', 'memtst_summary', 'memtst_init', 'memtst_put', 'memtst_get', 'memtst_bt', 'memtst_malloc', 'memtst_free', 'swap', 'fix', 'qsort', 'srand', 'rand', 'rnode_make', 'rnode_free', 'uc_len', 'uc_dec', 'ratom_copy', 'brk_len', 'ratom_read_brk', 'ratom_read', 'uc_beg', 'isword', 'brk_match', 'ratom_match', 'rnode_grp', 'rnode_atom', 'rnode_seq', 'rnode_parse', 'rnode_count', 're_insert', 'rnode_emitnorep', 'rnode_emit', 'regcomp', 'regfree', 're_rec', 're_recmatch', 'regexec', 'regerror', 'ic', 'setbuf', 'fgetc', 'getchar', 'ungetc', 'iint', 'istr', 'vfscanf', 'fscanf', 'scanf', 'vsscanf', 'sscanf', 'fgets', 'va_arg', 'fflush', 'whatisthis_0', 'oc', 'ostr', 'digits', 'oint', 'vfprintf', 'perror', 'vsnprintf', 'vsprintf', 'putc', 'puts', 'printf', 'fprintf', 'sprintf', 'snprintf', 'fputs', 'abs', 'labs', 'atexit', '__neatlibc_exit', 'exit', 'putstr', 'puti', 'puttz', 'strftime', 'strncpy', 'strcat', 'strstr', 'whatisthis_11', '_exit', 'whatisthis_14', 'read', 'write', 'gettimeofday', 'whatisthis_9', 'whatisthis_10', 'memset', 'memcpy', 'memtst_back', 'memcmp', 'mprotect', 'whatisthis_12', 'whatisthis_13', 'strlen', 'strncmp', 'strcpy', 'strchr', 'strcmp', 'wait']

libc_start_addr = 0x0060
current_addr = libc_start_addr

for sym in syms:
    idc.MakeCode(current_addr)
    idc.MakeFunction(current_addr)
    idc.MakeNameEx(current_addr, sym, idc.SN_NOWARN)
    func = idaapi.get_func(current_addr)  
    FC = idaapi.FlowChart(func)
    for block in FC: current_addr = max(current_addr, block.endEA)

print "done"
