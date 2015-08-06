
#ifndef _CCOLUMN_HPP
#define _CCOLUMN_HPP

class CColumn {
    // name
    // Type
    // Constraints
    // Default Value
    CTable *m_table;
    string m_name;

    public:
    CColumn(CTable* tbl,  string name){
        m_table = tbl;
        m_name = name;
    }
    CTable* table() { return m_table;}
    string name(){return m_name;}
};

#endif
