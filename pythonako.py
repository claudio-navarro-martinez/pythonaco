lista=[('a',1),('b',2),('c',3)]

df=pd.DataFrame(lista,columns=['col1','col2'])

df.groupby(['col1']).agg(['count','mean'])

-- Query sample v$session y conseguimos los SQL que estan
select /*+ ORDERED USE_NL(t) opt_param('_optimizer_sortmerge_join_enabled','false') opt_param('hash_join_enabled','false') NO_TRANSFORM_DISTINCT_AGG */ 
            sqlid , count(*) "COUNT", count(distinct r.rn) DISTCOUNT
        from
            (select /*+ no_unnest */ rownum rn from dual connect by level <= 10000) r
          , v$session t
        where status = 'ACTIVE' and (wait_class != 'Idle' or state != 'WAITING')
        group by
            sqlid
        order by
            "COUNT" desc, sqlid
