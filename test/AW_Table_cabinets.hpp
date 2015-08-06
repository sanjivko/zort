#ifndef __AW_Table_cabinets_HPP__
#define __AW_Table_cabinets_HPP__
class AW_Table_cabinets {
	public:
		void set_col_cabinet_type(int val){m_col_cabinet_type = val;}
		int get_col_cabinet_type(){return m_col_cabinet_type;}
		void set_col_pallet_id(int val){m_col_pallet_id = val;}
		void set_col_pallet_side(string val){m_col_pallet_side = val;}
		void set_col_cabinet_id(int val){m_col_cabinet_id = val;}
		string get_col_pallet_side(){return m_col_pallet_side;}
		string get_col_modify_time(){return m_col_modify_time;}
		string get_col_create_time(){return m_col_create_time;}
		int get_col_pallet_id(){return m_col_pallet_id;}
		void set_col_create_time(string val){m_col_create_time = val;}
		void set_col_modify_time(string val){m_col_modify_time = val;}
		int get_col_cabinet_id(){return m_col_cabinet_id;}
	private:
		string  m_col_modify_time
		string  m_col_pallet_side
		int  m_col_cabinet_id
		string  m_col_create_time
		int  m_col_cabinet_type
		int  m_col_pallet_id
};
#endif
