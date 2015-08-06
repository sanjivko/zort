#ifndef __AW_Table_cabinet_types_HPP__
#define __AW_Table_cabinet_types_HPP__

//class AW_Table_cabinet_types;

class AW_Table_cabinet_types:public CTable {
    private:
        AW_Table_cabinet_types() 
        {
            m_col_cabinet_type_code  = new CColumn(this, "cabinet_type_code");
        } 

    public:
        static AW_Table_cabinet_types *m_instance;

        string name(){
            return "cabinet_types";
        }

        CColumn* m_col_cabinet_type_code;

        static AW_Table_cabinet_types* getInstance(){
            if (!m_instance){
                m_instance = new AW_Table_cabinet_types();
            } 
            return m_instance;
        }
        
        CQuery* search()
        {
        }

        CQuery* insert()
        {
        }

        CQuery* del()
        {
        }

        CQuery* update()
        {
        }

/*
        int get_col_ct_id(){return m_col_ct_id;}
        void set_col_ct_id(int val){m_col_ct_id = val;}
        string get_col_cabinet_type_code(){return m_col_cabinet_type_code;}
        void set_col_attributes(string val){m_col_attributes = val;}
        void set_col_location_count(int val){m_col_location_count = val;}
        string get_col_storage_type(){return m_col_storage_type;}
        void set_col_cabinet_type_code(string val){m_col_cabinet_type_code = val;}
        string get_col_attributes(){return m_col_attributes;}
        int get_col_location_count(){return m_col_location_count;}
        void set_col_storage_type(string val){m_col_storage_type = val;}
    private:
        int  m_col_location_count
        string  m_col_cabinet_type_code
        int  m_col_ct_id
        string  m_col_attributes
        string  m_col_storage_type
*/
};

AW_Table_cabinet_types* AW_Table_cabinet_types::m_instance = 0;
#endif

