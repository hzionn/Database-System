from flask import Flask, render_template, request, redirect
from configurations import db, PLACES, PLACEOFOCCUR, tmp_data

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1 # to refresh immediately in development


@app.route('/')  # home page
def index():
    return render_template('index.html')


@app.route('/login')  # login page
def login():
    return render_template('login.html', places=PLACES)


@app.route('/greet', methods=["POST"])  # greet user and perform searching features
def greet():
    # name = request.args.get('name', 'user') # get method
    name = request.form.get('name')
    place = request.form.get('place')
    tmp_data['name'] = name
    tmp_data['place'] = place
    if not tmp_data['name'] or tmp_data['place'] not in PLACES: # make sure not missing any user input
        return render_template('missing_info.html')
    return render_template('greet.html', name=name, place=place)


@app.route('/back', methods=['POST'])
def back():
    redirect('/greet')


@app.route('/insert', methods=['POST'])
def insert():
    if True:
        # suspect
        # DELETE FROM SUSPECT WHERE S_ID = 's000';
        #'s000', 'HELEN', 'MALE', '20000102', 'Taipei', 'Student', 'TAIWAN', 'college', '0920666666', 'NORMAL', 'Yes', 'Neg'
        insert_suspect_S_ID = request.form.get('insert_suspect_S_ID')
        insert_suspect_S_Name = request.form.get('insert_suspect_S_Name')
        insert_suspect_S_Gender = request.form.get('insert_suspect_S_Gender')
        insert_suspect_S_Birth = request.form.get('insert_suspect_S_Birth')
        insert_suspect_S_Birthplace = request.form.get('insert_suspect_S_Birthplace')
        insert_suspect_S_Occ = request.form.get('insert_suspect_S_Occ')
        insert_suspect_S_Add = request.form.get('insert_suspect_S_Add')
        insert_suspect_Education_Level = request.form.get('insert_suspect_Education_Level')
        insert_suspect_Phone_Num = request.form.get('insert_suspect_Phone_Num')
        insert_suspect_Economic_Status = request.form.get('insert_suspect_Economic_Status')
        insert_suspect_Recidivism = request.form.get('insert_suspect_Recidivism')
        insert_suspect_Urine_Routine = request.form.get('insert_suspect_Urine_Routine')
    if True:
        # case
        # DELETE FROM CRIMINAL_CASE WHERE Case_ID = '5';
        # 'case5', '5', 'Drug', 's004', '20210903', 'TAINAN', '5', 'E5', '3', '8', '7'
        # INSERT INTO CRIMINAL_CASE (Case_Name, Case_ID, Case_Type, Sus_ID, TimeOfOccur, PlaceOfOccur, Drug_ID, Evidence_ID, Police_ID1, Police_ID2, Police_ID3) VALUES('case5', '5', 'Drug', 's004', '20210903', 'TAINAN', '5', 'E5', '3', '8', '7')
        insert_case_Case_Name = request.form.get('insert_case_Case_Name')
        insert_case_Case_ID = request.form.get('insert_case_Case_ID')
        insert_case_Case_Type = request.form.get('insert_case_Case_Type')
        insert_case_Sus_ID = request.form.get('insert_case_Sus_ID')
        insert_case_TimeOfOccur = request.form.get('insert_case_TimeOfOccur')
        insert_case_PlaceOfOccur = request.form.get('insert_case_PlaceOfOccur')
        insert_case_Drug_ID = request.form.get('insert_case_Drug_ID')
        insert_case_Evidence_ID = request.form.get('insert_case_Evidence_ID')
        insert_case_Police_ID1 = request.form.get('insert_case_Police_ID1')
        insert_case_Police_ID2 = request.form.get('insert_case_Police_ID2')
        insert_case_Police_ID3 = request.form.get('insert_case_Police_ID3')
    if True:
        insert_seizure_SCase_ID = request.form.get('insert_seizure_SCase_ID')
        insert_seizure_Exhibit_ID = request.form.get('insert_seizure_Exhibit_ID')
        insert_seizure_Related_Ob_1 = request.form.get('insert_seizure_Related_Ob_1')
        insert_seizure_Related_Ob_2 = request.form.get('insert_seizure_Related_Ob_2')
        insert_seizure_Related_Ob_3 = request.form.get('insert_seizure_Related_Ob_3')
        insert_seizure_Related_Ob_4 = request.form.get('insert_seizure_Related_Ob_4')
        insert_seizure_Related_Ob_5 = request.form.get('insert_seizure_Related_Ob_5')
    if True:
        insert_police_P_Name = request.form.get('insert_police_P_Name')
        insert_police_Department = request.form.get('insert_police_Department')
        insert_police_P_ID = request.form.get('insert_police_P_ID')
        insert_police_Degree = request.form.get('insert_police_Degree')
    if True:
        insert_d_exhibit_DCase_ID = request.form.get('insert_d_exhibit_DCase_ID')
        insert_d_exhibit_DExhibit_ID = request.form.get('insert_d_exhibit_DExhibit_ID')
        insert_d_exhibit_Drug = request.form.get('insert_d_exhibit_Drug')
        insert_d_exhibit_NetWeight = request.form.get('insert_d_exhibit_NetWeight')
        insert_d_exhibit_Weight = request.form.get('insert_d_exhibit_Weight')
        insert_d_exhibit_PreTestResult = request.form.get('insert_d_exhibit_PreTestResult')
        insert_d_exhibit_ProTestResult = request.form.get('insert_d_exhibit_ProTestResult')

    if insert_d_exhibit_DCase_ID and insert_d_exhibit_DExhibit_ID:
        db.execute("INSERT INTO DRUG_EXHIBIT (DCase_ID, DExhibit_ID, Drug, NetWeight, Weight, PreTestResult, ProTestResult) VALUES(?, ?, ?, ?, ?, ?, ?)", insert_d_exhibit_DCase_ID, insert_d_exhibit_DExhibit_ID, insert_d_exhibit_Drug, insert_d_exhibit_NetWeight, insert_d_exhibit_Weight, insert_d_exhibit_PreTestResult, insert_d_exhibit_ProTestResult)
        tmp_data['DExhibit_ID'] = 'ALL'
        return redirect('/result_d_exhibit')
    elif insert_case_Case_ID and insert_case_Case_Name:
        db.execute("INSERT INTO CRIMINAL_CASE (Case_Name, Case_ID, Case_Type, Sus_ID, TimeOfOccur, PlaceOfOccur, Drug_ID, Evidence_ID, Police_ID1, Police_ID2, Police_ID3) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", insert_case_Case_Name, insert_case_Case_ID, insert_case_Case_Type, insert_case_Sus_ID, insert_case_TimeOfOccur, insert_case_PlaceOfOccur, insert_case_Drug_ID, insert_case_Evidence_ID, insert_case_Police_ID1, insert_case_Police_ID2, insert_case_Police_ID3)
        tmp_data['Case_ID'] = 'ALL'
        return redirect('/result_case')
    elif insert_police_P_ID and insert_police_P_Name:
        db.execute("INSERT INTO POLICE (P_Name, Department, P_ID, Degree) VALUES(?, ?, ?, ?)", insert_police_P_Name, insert_police_Department, insert_police_P_ID, insert_police_Degree)
        tmp_data['P_ID'] = 'ALL'
        return redirect('/result_police')
    elif insert_seizure_SCase_ID and insert_seizure_Exhibit_ID:
        db.execute("INSERT INTO SEIZURE_of_EXHIBIT (SCase_ID, Exhibit_ID, Related_Ob_1, Related_Ob_2, Related_Ob_3, Related_Ob_4, Related_Ob_5) VALUES(?, ?, ?, ?, ?, ?, ?)", insert_seizure_SCase_ID, insert_seizure_Exhibit_ID, insert_seizure_Related_Ob_1, insert_seizure_Related_Ob_2, insert_seizure_Related_Ob_3, insert_seizure_Related_Ob_4, insert_seizure_Related_Ob_5)
        tmp_data['SCase_ID'] = 'ALL'
        return redirect('/result_seizure')
    elif insert_suspect_S_ID and insert_suspect_S_Name:
        db.execute("INSERT INTO SUSPECT (S_ID, S_Name, S_Gender, S_Birth, S_Birthplace, S_Occ, S_Add, Education_Level, Phone_Num, Economic_Status, Recidivism, Urine_Routine) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", insert_suspect_S_ID, insert_suspect_S_Name, insert_suspect_S_Gender, insert_suspect_S_Birth, insert_suspect_S_Birthplace, insert_suspect_S_Occ, insert_suspect_S_Add, insert_suspect_Education_Level, insert_suspect_Phone_Num, insert_suspect_Economic_Status, insert_suspect_Recidivism, insert_suspect_Urine_Routine)
        tmp_data['S_ID'] = 'ALL'
        return redirect('/result_suspect')


@app.route('/search', methods=["POST"]) # will not be render
def search():
    S_ID = request.form.get('S_ID')
    tmp_data['S_ID'] = S_ID

    DExhibit_ID = request.form.get('DExhibit_ID')
    tmp_data['DExhibit_ID'] = DExhibit_ID

    Case_ID = request.form.get('Case_ID')
    tmp_data['Case_ID'] = Case_ID
    
    P_ID = request.form.get('P_ID')
    tmp_data['P_ID'] = P_ID

    SCase_ID = request.form.get('SCase_ID')
    tmp_data['SCase_ID'] = SCase_ID

    if S_ID:
        return redirect('/result_suspect')
    elif DExhibit_ID:
        return redirect('/result_d_exhibit')
    elif Case_ID:
        return redirect('/result_case')
    elif P_ID:
        return redirect('/result_police')
    elif SCase_ID:
        return redirect('/result_seizure')
    elif not S_ID and not DExhibit_ID and not Case_ID and not P_ID and not SCase_ID:
        return render_template('/missing_info_all.html')


@app.route('/advanced_search', methods=['POST'])
def advanced_search():
    Case_ID_advanced = request.form.get('Case_ID')
    tmp_data['Case_ID_advanced'] = Case_ID_advanced
    place_of_occur = request.form.get('place_of_occur')
    tmp_data['place_of_occur'] = place_of_occur
    if Case_ID_advanced:
        return redirect('/result_case_advanced')
    elif place_of_occur:
        return redirect('/result_place_advanced')


@app.route('/insert_suspect', methods=['POST'])
def insert_suspect():
    return render_template('insert/insert_suspect.html')

@app.route('/insert_case', methods=['POST'])
def insert_case():
    return render_template('insert/insert_case.html')

@app.route('/insert_d_exhibit', methods=['POST'])
def insert_d_exhibit():
    return render_template('insert/insert_d_exhibit.html')

@app.route('/insert_police', methods=['POST'])
def insert_police():
    return render_template('insert/insert_police.html')

@app.route('/insert_seizure', methods=['POST'])
def insert_seizure():
    return render_template('insert/insert_seizure.html')


@app.route('/result_suspect')
def result_suspect():
    if tmp_data['S_ID'] == 'ALL':
        result_suspect = db.execute("SELECT * FROM SUSPECT")
        return render_template('result/result_suspect.html', result_suspect=result_suspect)
    result_suspect = db.execute("SELECT * FROM SUSPECT WHERE S_ID = ?", tmp_data['S_ID'])
    return render_template('result/result_suspect.html', result_suspect=result_suspect)

@app.route('/result_case')
def result_case():
    if tmp_data['Case_ID'] == 'ALL':
        result_case = db.execute("SELECT * FROM CRIMINAL_CASE")
        return render_template('result/result_case.html', result_case=result_case)
    result_case = db.execute("SELECT * FROM CRIMINAL_CASE WHERE Case_ID = ?", tmp_data['Case_ID'])
    return render_template('result/result_case.html', result_case=result_case)

@app.route('/result_d_exhibit')
def result_d_exhibit():
    if tmp_data['DExhibit_ID'] == 'ALL':
        result_d_exhibit = db.execute("SELECT * FROM DRUG_EXHIBIT")
        return render_template('result/result_d_exhibit.html', result_d_exhibit=result_d_exhibit)
    result_d_exhibit = db.execute("SELECT * FROM DRUG_EXHIBIT WHERE DExhibit_ID = ?", tmp_data['DExhibit_ID'])
    return render_template('result/result_d_exhibit.html', result_d_exhibit=result_d_exhibit)

@app.route('/result_police')
def result_police():
    if tmp_data['P_ID'] == 'ALL':
        result_police = db.execute("SELECT * FROM POLICE")
        return render_template('result/result_police.html', result_police=result_police)
    result_police = db.execute("SELECT * FROM POLICE WHERE P_ID = ?", tmp_data['P_ID'])
    return render_template('result/result_police.html', result_police=result_police)

@app.route('/result_seizure')
def result_seizure():
    if tmp_data['SCase_ID'] == 'ALL':
        result_seizure = db.execute("SELECT * FROM SEIZURE_of_EXHIBIT")
        return render_template('result/result_seizure.html', result_seizure=result_seizure)
    result_seizure = db.execute("SELECT * FROM SEIZURE_of_EXHIBIT WHERE SCase_ID = ?", tmp_data['SCase_ID'])
    return render_template('result/result_seizure.html', result_seizure=result_seizure)


@app.route('/result_place_advanced')
def result_place_advanced():
    result_place_advanced = db.execute("SELECT * FROM CRIMINAL_CASE WHERE PlaceOfOccur = ?", tmp_data['place_of_occur'])
    count = db.execute("SELECT COUNT(*) FROM CRIMINAL_CASE WHERE PlaceOfOccur = ?", tmp_data['place_of_occur'])
    return render_template('result/result_place_advanced.html', result_place_advanced=result_place_advanced, count=count)


@app.route('/result_case_advanced')
def result_case_advanced():
    if tmp_data['Case_ID_advanced'] == 'ALL':
        result_c_advanced = db.execute("SELECT * FROM CRIMINAL_CASE")
        result_d_advanced = db.execute("SELECT * FROM DRUG_EXHIBIT")
        result_s_advanced = db.execute("SELECT * FROM SEIZURE_of_EXHIBIT")
        return render_template('result/result_case_advanced.html', result_c_advanced=result_c_advanced, result_d_advanced=result_d_advanced, result_s_advanced=result_s_advanced)
    result_c_advanced = db.execute("SELECT * FROM CRIMINAL_CASE WHERE Case_ID = ?", tmp_data['Case_ID_advanced'])
    result_d_advanced = db.execute("SELECT * FROM DRUG_EXHIBIT WHERE DCase_ID = ?", tmp_data['Case_ID_advanced'])
    result_s_advanced = db.execute("SELECT * FROM SEIZURE_of_EXHIBIT WHERE SCase_ID = ?", tmp_data['Case_ID_advanced'])
    return render_template('result/result_case_advanced.html', result_c_advanced=result_c_advanced, result_d_advanced=result_d_advanced, result_s_advanced=result_s_advanced)


@app.route('/delete', methods=['POST'])
def delete():
    s_id = request.form.get('s_id')
    tmp_data['s_id'] = s_id
    dexhibit_ID = request.form.get('dexhibit_ID')
    tmp_data['dexhibit_ID'] = dexhibit_ID
    case_ID = request.form.get('case_ID')
    tmp_data['case_ID'] = case_ID
    p_id = request.form.get('p_id')
    tmp_data['p_id'] = p_id
    scase_id = request.form.get('scase_id')
    tmp_data['scase_id'] = scase_id
    if s_id:
        db.execute("DELETE FROM SUSPECT WHERE S_ID = ?", tmp_data['s_id'])
        return redirect('/result_suspect')
    elif dexhibit_ID:
        db.execute("DELETE FROM DRUG_EXHIBIT WHERE DExhibit_ID = ?", tmp_data['dexhibit_ID'])
        return redirect('/result_d_exhibit')
    elif case_ID:
        db.execute("DELETE FROM CRIMINAL_CASE WHERE Case_ID = ?", tmp_data['case_ID'])
        return redirect('/result_case')
    elif p_id:
        db.execute("DELETE FROM POLICE WHERE P_ID = ?", tmp_data['p_id'])
        return redirect('t/result_police')
    elif scase_id:
        db.execute("DELETE FROM SEIZURE_of_EXHIBIT WHERE SCase_ID = ?", tmp_data['scase_id'])
        return redirect('/result_seizure')


@app.route('/advanced')
def advanced():
    tmp_data['state'] = 'advanced'
    return render_template('/advanced.html', name=tmp_data['name'], place=tmp_data['place'], places=PLACEOFOCCUR)


if __name__ == '__main__':
    app.run()
