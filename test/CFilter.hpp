#ifndef __CFILTER_HPP__
#define __CFILTER_HPP__

#include <string>

using namespace std;
class CFilter
{
    private:
        string m_filter_string;

    public:
        string str() const {
            return m_filter_string;
        }

        CFilter(string s){
            m_filter_string = "(" + s + ")";
        }

        CFilter(const CFilter& sfilter){
            m_filter_string = "(" + sfilter.str() + ")";
        }


        CFilter OR(CFilter sfilter) {
            m_filter_string += " OR (" + sfilter.str() + ")";
            return *this;
        }

        CFilter AND(CFilter sfilter) {
            m_filter_string += " AND (" + sfilter.str() + ")";
            return *this;
        }

        CFilter OR(string s){
            m_filter_string += " OR (" + s + ")";
            return *this;
        }

        CFilter AND(string s){
            m_filter_string += " AND (" + s + ")";
            return *this;
        }
};

//CFilter(col.eq("")).OR(col.eq(""))
//CFilter(col.eq("")).OR(CFilter(col.eq("")))
//CFilter(col.eq("")).OR(CFilter(col.eq("")).AND(col.eq('')))

#endif
