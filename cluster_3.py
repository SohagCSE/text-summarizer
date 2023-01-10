class cluster_3:

    def __init__(self,listt):
        self.listt = listt


    def k_mean_3(self):
        m_1,m_2,m_3 = self.mean_init()

        p_m1 = 0
        p_m2 = 0
        p_m3 = 0
        while(p_m1 != m_1 or p_m2 != m_2 or p_m3 != m_3):
            p_m1 = m_1
            p_m2 = m_2
            p_m3 = m_3

            list_1,list_2,list_3 = self.clustering(m_1,m_2,m_3)    # convert a list into 3 cluster
            m_1 = self.avr(list_1)
            m_2 = self.avr(list_2)
            m_3 = self.avr(list_3)

            #print(list_1,"\n",list_2,"\n",list_3,"\n------------")
            
        return list_1,list_2,list_3        # final output for cluster
    

    def mean_init(self):
        num_list = list(zip(*(self.listt)))
        num_list = list(num_list[1])
        num_list.sort()
        return num_list[0],num_list[round(len(num_list)/2)], num_list[len(num_list)-1]
    

    def clustering(self,m1,m2,m3):
        list_1 = []
        list_2 = []
        list_3 = []
        for v in self.listt:
            d1 = abs(v[1] - m1)
            d2 = abs(v[1] - m2)
            d3 = abs(v[1] - m3)

            if d1<=d2 and d1<=d3:
                list_1.append(v)
            elif d2<=d2 and d2<=d3:
                list_2.append(v)
            else:
                list_3.append(v)
                
        return list_1,list_2,list_3




    def avr(self,lst):
        if len(lst) == 0:
            return 0
        s = 0
        for x in lst:
            s += x[1]
        return(s/len(lst))






