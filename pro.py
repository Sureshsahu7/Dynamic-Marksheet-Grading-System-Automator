
from numpy import NAN
import pandas as pd
import os
import re
import shutil
import xlsxwriter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def generate_marksheet(p,n):
    roll = pd.read_csv('sample_input/master_roll.csv')
    response = pd.read_csv('sample_input/responses.csv')
    response.rename(columns = {'Roll Number':'roll'}, inplace = True)
    res = pd.merge(response, roll,how='outer', on=["roll"])
    s=1
    for i in range(7,35):
     res.rename( columns={f'Unnamed: {i}':f'q{s}'}, inplace=True )
     s+=1
    if  os.path.exists('sample_output'):
        shutil.rmtree('sample_output')
    os.makedirs('sample_output')
    for index, row in res.iterrows(): 
           a=str(row['roll'])
           b=str(row['name'])
           if pd.isnull(row['Score']):
               workbook = xlsxwriter.Workbook(f'sample_output/{a}_ABSENT.xlsx')
               worksheet = workbook.add_worksheet()
               workbook.close()
           else:
               c=str(row['Score'])
               st='(.*?) / 140'
               mat=re.match(st,c)
               if mat:
                   mrk=int(mat.group(1))
               bs=mrk/5
               pve=bs*p
               rit=str(mrk/5)
               lft=res.loc[[index]].isna().sum().sum()
               wrg=28-bs-lft
               nve=wrg*n
               tot=pve+nve
               workbook = xlsxwriter.Workbook(f'sample_output/{a}.xlsx')
               worksheet = workbook.add_worksheet()
               worksheet.set_column('A:E', 15)
               worksheet.write('C5', 'MARKSHEET')
               image_width = 853
               image_height = 126
               cell_width = 87
               cell_height = 15
               x_scale = cell_width/image_width
               y_scale = cell_height/image_height
               worksheet.insert_image('A1', 'pic.png', {'x_scale':0.65 , 'y_scale': y_scale*6+0.05})
               cell_format5 = workbook.add_format({'bold': True,'font_size':12,'font_name':'Century','align':'left'})
               cell_format1 = workbook.add_format({'bold': True,'font_size':12,'font_name':'Century'})
               cell_format3 = workbook.add_format({'bold': True,'font_size':12,'font_name':'Century','align':'center','border':1})
               cell_format2= workbook.add_format({'font_size':12,'font_name':'Century','align':'right'})
               cell_format6= workbook.add_format({'font_size':12,'font_name':'Century','align':'centre','border':1})
               cell_format7= workbook.add_format({'font_size':12,'font_name':'Century','align':'centre','font_color':'green','border':1})
               cell_format8= workbook.add_format({'font_size':12,'font_name':'Century','align':'centre','font_color':'red','border':1})
               cell_format9= workbook.add_format({'font_size':12,'font_name':'Century','align':'centre','font_color':'blue','border':1})
               cell_format10= workbook.add_format({'font_size':12,'font_name':'Century','align':'centre'})
               cell_format4= workbook.add_format({'border':1})
               worksheet.write_string('A6','Name:',cell_format2)
               worksheet.write_string('A7','Roll No:',cell_format2)
               worksheet.write_string('A10','No.',cell_format3)
               worksheet.write_string('A9','',cell_format4)
               worksheet.write_string('A11','Marking',cell_format3)
               worksheet.write_string('A12','Total',cell_format3)
               worksheet.write_string('D6','Exam:',cell_format2)
               worksheet.write_string('E6','quiz',cell_format1)
               worksheet.write_string('B9','Right',cell_format3)
               worksheet.write_string('C9','Wrong',cell_format3)
               worksheet.write_string('C10',str(wrg),cell_format8)
               worksheet.write_string('C11',str(n),cell_format8)
               worksheet.write_string('D9','Not Attempt',cell_format3)
               worksheet.write_string('D10',str(lft),cell_format6)
               worksheet.write_string('D11','0',cell_format6)
               worksheet.write_string('E9','Max',cell_format7)
               worksheet.write_string('E10','28',cell_format6)
               worksheet.write_string('E11','',cell_format4)
               worksheet.write_string('D12','',cell_format4)
               worksheet.write_string('B10',str(rit),cell_format7)
               worksheet.write_string('B11',str(p),cell_format7)
               worksheet.write_string('B6',f'{b}',cell_format5)
               worksheet.write_string('B7',f'{a}',cell_format5)
               worksheet.write_string('B12',f'{pve}',cell_format7)
               worksheet.write_string('C12',f'{nve}',cell_format8)
               worksheet.write_string('E12',f'{tot}'+f'/{28*p}',cell_format9)
               worksheet.write_string('A15','Student Ans',cell_format3)
               for i in range(16,41):
                   if pd.isnull(row[f'q{i-15}']):
                       worksheet.write_string(f'A{i}','')
                   else:
                        worksheet.write_string(f'A{i}',str(row[f'q{i-15}']),cell_format10)
                   worksheet.write_string(f'B{i}',str(res.loc[0,f'q{i-15}']),cell_format9)
               for j in range(16,19):
                   if pd.isnull(row[f'q{j+10}']):
                       worksheet.write_string(f'D{j}','')
                   else:
                       worksheet.write_string(f'D{j}',str(row[f'q{j+10}']),cell_format10)
                   worksheet.write_string(f'E{j}',str(res.loc[0,f'q{j+10}']),cell_format9)
               worksheet.conditional_format('A16:A40', {'type':'formula',
                                           'criteria':'=A16=B16',
                                           'format':cell_format7})
               worksheet.conditional_format('A16:A40', {'type':'formula',
                                           'criteria':'=A16<>B16',
                                           'format':cell_format8})
               worksheet.conditional_format('D16:D18', {'type':'formula',
                                           'criteria':'=D16=E16',
                                           'format':cell_format7})
               worksheet.conditional_format('D16:D18', {'type':'formula',
                                           'criteria':'=D16<>E16',
                                           'format':cell_format8})

               worksheet.write_string('B15','Correct Ans',cell_format3)
               worksheet.write_string('D15','Student Ans',cell_format3)
               worksheet.write_string('E15','Correct Ans',cell_format3)
               workbook.close()

               
def concise_mrks(p,n):
    
    response = pd.read_csv('sample_input/responses.csv')
    response.rename(columns = {'Roll Number':'roll'}, inplace = True)
    
    s=1
    for i in range(7,35):
     response.rename( columns={f'Unnamed: {i}':f'q{s}'}, inplace=True )
     s+=1
    if  os.path.exists(r'sample_output/concise_marksheet.csv'):
        os.remove(r'sample_output/concise_marksheet.csv')
    afngv=[]
    statans=[]
    gscore=[]
    for index, row in response.iterrows(): 
          
           c=str(row['Score'])
           st='(.*?) / 140'
           mat=re.match(st,c)
           if mat:
               mrk=int(mat.group(1))
           bs=mrk/5
           pve=bs*p
           rit=str(mrk/5)
           lft=response.loc[[index]].isna().sum().sum()
           wrg=28-bs-lft
           nve=wrg*n
           tot=pve+nve
           tototot=28*p
           
           afngv.append(f'{tot} / {tototot}')
           gscore.append(f'{pve} / {tototot}')
           statans.append(f'({bs} , {wrg} , {lft})')
    response.rename(columns={'Score':'Google_Score'},inplace=True)

    response['Google_Score']=gscore
    
    response['Score_after_negative']=afngv 
    response['StatusAns']=statans
    response.to_csv(r'sample_output/concise_marksheet.csv')

def sendmail():

    curntdirectory = os.getcwd()
    responsedirectory= curntdirectory+'/sample_input'
    os.chdir(responsedirectory)
    
    
    ress = pd.read_csv('responses.csv',index_col='Timestamp')
    
    email = ress["Email address"].values.tolist()
    IITP_mail =ress["IITP webmail"].values.tolist() 
    ROLLNUM = ress["Roll Number"].values.tolist()
    dict={}
    for i in range(0,len(ROLLNUM)):
        dict[ROLLNUM[i]]=[IITP_mail[i],email[i]]
    os.chdir(curntdirectory) 
    myoutput_path = curntdirectory+'/sample_output'
    os.chdir(myoutput_path)
    for i in range(0,len(ROLLNUM)): 
        for j in range(0,2):  
            sender = "sureshtest8202@gmail.com"
            reciever = dict[ROLLNUM[i]][j]
            msg = MIMEMultipart() 
            msg['From'] = sender 
            msg['To'] = reciever 
            msg['Subject'] = "Quiz marks Attached"
            body = "Your Quiz marks Attached.Verify it."
            msg.attach(MIMEText(body, 'plain')) 
            filename = "{}.xlsx".format(ROLLNUM[i])
            attachment = open("{}.xlsx".format(ROLLNUM[i]), "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender, "Mahe@8202")
            text = msg.as_string()
            s.sendmail(sender, reciever, text)
            s.quit()




               
               
    
               
        
               
    
           
           
       






