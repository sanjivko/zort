# zort
The objective is the abstract database queries from programming and make it easier to migrate.Writing queries in C++ code poses delays during migration of databases which needs to be handled in a seamless way.

I want to use the power of C++ strong typing to ensure queries generated are syntactically correct. 

To give an idea of how queries should be wriiten with this library, here are few examples. 

"select pallet_id from cabinets where ((A=B and C=D) OR (E=F))"

q.select(CTable::getInstance()->m_col_pallet_id)->where(CFilter("A=B").AND("C=D").OR("E=F"))

There are various features that need to be added to this, e.g joins, subquery, etc. The idea is to make the api easy to understand and robust. 

