#-*-coding:utf-8-*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import wenjuan_content
import traceback
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

{{  request.user.has_perm  }}
def test(request):
    if request.method == "GET":
        print "111111111111111"
        print request.user
        print "wenjuan_del",request.user.has_perm("app.wenjuan_del")
        print "wenjuan_update", request.user.has_perm("app.wenjuan_update")
        print "222222222222222"



def desc(request):
    if request.method == "GET":
       print request.body
       return render(request,"desc.html")
       #return  HttpResponse(request.body)




def admin(request):
    if request.method == "GET":
        all_dic={}
        all_dic_two = {}
        mo_tai_list=[]
        all_list=[]
        mo_tai_res = wenjuan_content.objects.filter().values()
        for mt in  mo_tai_res:
            mo_tai_dic = {}
            mo_tai_dic["sub_line"] = mt["sub_line"]
            mo_tai_dic["id"] = mt["id"]
            jingli = mt["jingli"].split("*")[0]

            jingli_one = jingli.split(";")
            for i in jingli_one:
                if "产品经理_1" in i:
                    mo_tai_dic["cpjl_1"] = i.split(":")[-1]
                if "综合" in i:
                    mo_tai_dic["zh_1"] = i.split(":")[-1]
                if "效率" in i:
                    mo_tai_dic["xl_1"] = i.split(":")[-1]
                if "专业" in i:
                    mo_tai_dic["zh_1"] = i.split(":")[-1]
                if "其他" in i:
                    mo_tai_dic["textarea_1"] = i.split(":")[-1]
            all_list.append(mo_tai_dic)








        # all_list=[]
        # all_dic_one["id"]="22"
        # all_dic_one["jingli_1"]="saber22"
        # all_dic_one["jingli_2"]="lmx22"
        # all_list.append(all_dic_one)
        #
        # all_dic_two["id"] = "23"
        # all_dic_two["jingli_1"] = "saber23"
        # all_dic_two["jingli_2"] = "lmx23"
        # all_list.append(all_dic_two)






        return render(request,"quest_inve_content.html",locals())
    # if request.method == "POST":
    #     res = wenjuan_content.objects.filter().values()
    #     return  HttpResponse(json.dumps(res))


def q_inves(request):

    to_html = []
    # mo_tai_list=[]

    res = wenjuan_content.objects.filter().values()
    for content in res:
        dic_content={}
        # mo_tai_k_dic={}
        # mo_tai_k_dic["sub_line"] =  content["sub_line"]
        # mo_tai_k_dic["id"] = content["id"]

        # content["auto_time"] = str(content["auto_time"])[:30]+ '......'
        # dic_content["sub_line"] = content["sub_line"]
        # dic_content["jingli"] = content["jingli"][:30]+ '......'
        # dic_content["qdzz"] = content["qdzz"][:30]+ '......'
        # dic_content["qdxzcy"] = content["qdxzcy"][:30]+ '......'
        # dic_content["javazz"] = content["javazz"][:30]+ '......'
        # dic_content["javaxzcy"] = content["javaxzcy"][:30]+ '......'
        # dic_content["cszz"] = content["cszz"][:30]+ '......'
        # dic_content["csxzcy"] = content["csxzcy"][:30]+ '......'
        # dic_content["last_content"] = content["last_content"][:30]+ '......'
        # dic_content["desc"] = content["id"]
        # to_html.append(dic_content)
        content["auto_time"] = str(content["auto_time"])
        dic_content["sub_line"] = content["sub_line"]
        dic_content["jingli"] = content["jingli"]
        dic_content["qdzz"] = content["qdzz"]
        dic_content["qdxzcy"] = content["qdxzcy"]
        dic_content["javazz"] = content["javazz"]
        dic_content["javaxzcy"] = content["javaxzcy"]
        dic_content["cszz"] = content["cszz"]
        dic_content["csxzcy"] = content["csxzcy"]
        dic_content["last_content"] = content["last_content"]
        dic_content["desc"] = content["id"]
        to_html.append(dic_content)

    return HttpResponse(json.dumps(to_html))





def index_wenjuan(request):
    return render(request,"wenjuan.html")

def res(request):
    return render(request,"res.html")

def api(request):
    try:

        res_str = request.POST.get("ssss")
        res_dic =json.loads(res_str)
        ##### 第一页/共九页产品经理调查页
        sub_line = res_dic["sub_line"]
        page_one_cpjl = res_dic["page_one_cpjl"]
        content_one = """
        产品经理_1：{};
        此产品经理综合:{};
        此产品经理专业:{};
        此产品经理效率:{};
       
        此产品经理团队精神:{};
        有其它话想说 :{}
        """.format(page_one_cpjl,res_dic["input_page_one_one"],res_dic["input_page_one_two"],res_dic["input_page_one_three"],res_dic["input_page_one_four"],res_dic["one_page_text"])

        ##### 第二页/共九页产品经理调查页
        content_two = """
        产品经理_2:{};
        此产品经理综合:{};
        此产品经理专业:{};
        此产品经理效率:{};
     
       此产品经理团队精神:{};
        有其它话想说 :{}
        """.format(res_dic["page_two_cpjl"],res_dic["input_page_two_one"],res_dic["input_page_two_two"],res_dic["input_page_two_three"],res_dic["input_page_two_four"],res_dic["two_page_text"])

        ##### 第三页/共九页前端
        content_three = """
        前端组长：{};
        上面同学综合:{};
        上面同学项目管理能力:{};
        上面同学专业性:{};
        上面同学效率:{};
        上面同学团队精神:{};
        有其它话想说 :{}
        """.format(res_dic["page_three_cpjl"],res_dic["input_page_three_one"],res_dic["input_page_three_two"],res_dic["input_page_three_three"],res_dic["input_page_three_four"],res_dic["input_page_three_five"],res_dic["three_page_text"])





        ##### 第四页/共九页前端
        # 第一个前端工程师
        content_four_one = """
        前端_1{};
        上面同学综合:{};
        上面同学专业性:{};
        上面同学效率:{};
        上面同学团队精神:{};
        """.format(res_dic["page_four_one_cpjl"], res_dic["input_page_four_one_one"],
           res_dic["input_page_four_one_two"], res_dic["input_page_four_one_three"],
           res_dic["input_page_four_one_four"])
        ##### 第四页/共九页前端
        # 第二个前端工程师
        content_four_two = """
        前端_2{};
        上面同学综合:{};
        上面同学专业性:{};
        上面同学效率:{};
        上面同学团队精神:{};
        """.format(res_dic["page_four_two_cpjl"], res_dic["input_page_four_two_one"],
           res_dic["input_page_four_two_two"], res_dic["input_page_four_two_three"],
           res_dic["input_page_four_two_four"])




        ##### 第五页/共九页
        #java
        content_five = """
        java 组长：{};
        上面同学综合:{};
        上面同学项目管理能力:{};
        上面同学专业性:{};
        上面同学效率:{};
        上面同学团队精神:{};
        有其它话想说 :{};
        """.format(res_dic["page_five_cpjl"], res_dic["input_page_five_one"],
               res_dic["input_page_five_two"], res_dic["input_page_five_three"],res_dic["input_page_five_four"],
               res_dic["input_page_five_five"],res_dic["five_page_text"])
        #第六页
        #java 小组1
        content_six_one = """
        java_1:{};
        上面同学综合:{};
        上面同学专业性:{};
        上面同学效率:{};
        上面同学团队精神:{};
        """.format(res_dic["page_six_one_cpjl"], res_dic["input_page_six_one_one"],
           res_dic["input_page_six_one_two"], res_dic["input_page_six_one_three"],
           res_dic["input_page_six_one_four"])

        #java 小组2
        content_six_two = """
        java_2:{};
        上面同学综合:{};
        上面同学专业性:{};
        上面同学效率:{};
        上面同学团队精神:{}
        """.format(res_dic["page_six_two_cpjl"], res_dic["input_page_six_two_one"],
           res_dic["input_page_six_two_two"], res_dic["input_page_six_two_three"],
           res_dic["input_page_six_two_four"])


        #第七页
        # 测试
        content_seven = """
        测试组长：{};
        上面同学综合:{};
        上面同学项目管理能力:{};
        上面同学专业性:{};
        上面同学效率:{};
        上面同学团队精神:{};
        有其它话想说 :{}
        """.format(res_dic["seven_page_text"], res_dic["input_page_seven_one"],
                  res_dic["input_page_seven_two"], res_dic["input_page_seven_three"],
                  res_dic["input_page_seven_four"],
                  res_dic["input_page_seven_five"], res_dic["seven_page_text"])


        #测试 小组1
        #第八页
        content_eight_one = """
        测试组长：{};
        上面同学综合:{};
        上面同学专业性:{};
        上面同学效率:{};
        上面同学团队精神:{}
        """.format(res_dic["page_eight_one_cpjl"], res_dic["input_page_eight_one_one"],
           res_dic["input_page_eight_one_two"], res_dic["input_page_eight_one_three"],
           res_dic["input_page_eight_one_four"])


        #第九页 最后一页
        iwang = res_dic["iwang"]
        last_select = res_dic["last_select"]
        chage_reasons = res_dic["chage_reasons"]
        whoiam = res_dic["whoiam"]
        changelevel = res_dic["changelevel"]
        changelevel_reason = res_dic["changelevel_reason"]
        pingjiares = res_dic["pingjiares"]
        last_content = """
        我想留在本组：{};
        我想去的产品线：{};
        申请换组理由：{};
        我是谁：{};
        我想当组长/项目负责人:{};
        申请当组长和项目负责人理由_to :{};
        我上述评价内容客观_tt：{}
        """.format(iwang,last_select,chage_reasons,whoiam,changelevel,changelevel_reason,pingjiares)







        jingli = content_one +"*"+ content_two
        qdzz = content_three
        qdxzcy =  content_four_one +  content_four_two
        javazz = content_five
        javaxzcy = content_six_one  + content_six_two

        cszz = content_seven
        csxzcy = content_eight_one


        print "sub_line",sub_line
        print "jingli", jingli
        print "qdzz", qdzz
        print "qdxzcy", qdxzcy
        print "javazz", javazz
        print "javaxzcy", javaxzcy
        print "cszz", cszz
        print "csxzcy", csxzcy
        print "content_eight_one", content_eight_one
        print "last_content", last_content


        content = wenjuan_content()
        content.sub_line = sub_line
        content.jingli = jingli
        content.qdzz = qdzz
        content.qdxzcy = qdxzcy

        content.javazz =javazz
        content.javaxzcy = javaxzcy

        content.cszz = cszz
        content.csxzcy = csxzcy

        content.last_content = last_content
        content.save()
        res = {"status":"ok"}
        return HttpResponse(json.dumps(res))
    except Exception:
        print traceback.format_exc()






####

# mo_tai_list=[]
# mo_tai_res = wenjuan_content.objects.filter().values()
# for mt in  mo_tai_res:
#     mo_tai_dic = {}
#     mo_tai_dic["sub_line"] = mt["sub_line"]
#     mo_tai_dic["id"] = mt["id"]
#     jingli = mt["jingli"].split("*")
#     jingli_one = jingli.split(";")








