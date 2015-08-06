#ifndef _CQUERY_HPP__
#define _CQUERY_HPP__

#include <string>
#include <vector>
#include <iostream>
#include "CTable.hpp"
#include "CColumn.hpp"

using namespace std;

class CQuery
{
        string m_qry;

        vector<CTable*> m_tbls;
        vector<CColumn*> m_cols;

        string gen_qry(){
            string t = "select ";
            for (int i = 0; i < m_cols.size(); i++) {
                if (i > 0)
                    t += ",";
                t += m_cols[i]->name()+" "; 
            }

            t += " from ";
            for (int i = 0; i < m_tbls.size(); i++) {
                if (i > 0)
                    t += ",";
                t += m_tbls[i]->name()+" "; 
            }

            //where clause

            return t;
        }
    public:
        //CResult execute(CDbConn *conn){
        void execute(){
            string qry = gen_qry();
            cout << "Query is:" << qry << endl; 
        }

        CQuery* table(CTable* t){
        }

        CQuery* select(CColumn* col){
            m_tbls.push_back(col->table());
            m_cols.push_back(col);
    
            return this;
        }

        CQuery* filter(){

        }
};

#endif
