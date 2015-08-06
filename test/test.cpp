
#include "CQuery.hpp"
#include "Table1.hpp"
#include "Table2.hpp"


int main()
{
    CQuery q;
    q.select(AW_Table_cabinet_types::getInstance()->m_col_cabinet_type_code);
    q.select(AW_Table_cabinets::getInstance()->m_col_pallet_id);
    q.execute();
}
