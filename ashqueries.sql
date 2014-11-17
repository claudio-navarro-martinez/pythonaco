select  
                                     systimestamp, saddr, %sid%, serial#, audsid, paddr, user#,
                                     username, command, ownerid, taddr, lockwait,
                                     status, server, schema#, schemaname, osuser,
                                     process, machine, terminal, program, type,
                                     sql_address, sql_hash_value, sql_id, sql_child_number,
                                     prev_sql_addr, prev_hash_value, prev_sql_id,
                                     prev_child_number, module, module_hash, action,
                                     action_hash, client_info, fixed_table_sequence,
                                     row_wait_obj#, row_wait_file#, row_wait_block#,
                                     row_wait_row#, logon_time, last_call_et, pdml_enabled,
                                     failover_type, failover_method, failed_over,
                                     resource_consumer_group, pdml_status, pddl_status,
                                     pq_status, current_queue_duration, client_identifier,
                                     blocking_session_status, blocking_instance,
                                     blocking_session, seq#, event#, case when state = 'WAITING' then event else 'ON CPU' end, p1text, p1,
                                     p1raw, p2text, p2, p2raw, p3text, p3, p3raw,
                                     wait_class_id, wait_class#, case when state = 'WAITING' then wait_class else 'ON CPU' end, wait_time,
                                     seconds_in_wait, state, service_name, sql_trace,
                                     sql_trace_waits, sql_trace_binds
                                     
                           from   v$session
                           where ....
                           
 select sql_id, sql_child_number,count(*) ocurrences
 from ash_array
 group by sql_id, sql_child_number
 order by count(*) desc
 
 
 ---------------------
 
  select 'STAT' as type
                  ,      sn.name
                  ,      ss.value
        from   v$statname sn
        ,      v$sysstat  ss
        where  sn.statistic# = ss.statistic#
  union all
  select 'LATCH'
          ,      name
          ,      gets
        from   v$latch
  union all
  select 'TIMER'
          ,      'moats timer'
          ,      hsecs
        from   v$timer
        
  select event,wait_class,count(*)
        from stats_array
        group by event,wait_class
        order by count(*) desc
