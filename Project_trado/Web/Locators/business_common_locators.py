from selenium.webdriver.common.by import By


class Promo_Locators:

    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    common_Question=(By.XPATH,"//h3[contains(text(),'שאלות נפוצות')]")
    for_all_Question=(By.XPATH, "//a[contains(text(),'לכל השאלות')]")
    men_image=(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/img[2]")
    women_image=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/img[1]")
    logo_Trado=(By.XPATH,"//header/div[1]/div[1]/a[2]/div[1]/a[1]/img[1]")
    product_page=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]")
    product_upload_page=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/button[1]")
    question_link=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[3]/div[1]/div[2]/a[1]")
    business_interface_link=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[3]/div[1]/div[1]/a[5]")
    common_Question_link=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[3]/div[1]/div[2]/a[1]")
    blue_box_logo=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[3]/div[1]/div[4]")
    whatsapp_logo=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[4]")
    whatsapp_logo_link=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[4]/div[2]/*[1]")
    whatsapp_type=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[4]/div[1]/div[3]/input[1]")
    whatsapp_send_button=(By.XPATH,"//button[contains(text(),'שלח')]")
    business_interface_firstname=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]"
                                           "/div[1]/div[1]/span[1]/input[1]")
    business_interface_lastname=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]"
                                          "/form[1]/div[1]/div[2]/span[1]/input[1]")
    business_interface_HTR=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]"
                                     "/form[1]/div[1]/div[3]/span[1]/input[1]")
    name_of_the_business=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]"
                                   "/form[1]/div[1]/div[4]/span[1]/input[1]")
    select_catagories=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]"
                                "/div[1]/div[5]/div[1]/select[1]")
    phone_number=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]"
                           "/div[2]/form[1]/div[1]/div[6]/span[1]/input[1]")
    business_interface_email=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]"
                                       "/div[1]/div[7]/span[1]/input[1]")
    city_business=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]"
                            "/div[1]/div[1]/span[1]/input[1]")
    street_business=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]"
                              "/form[1]/div[2]/div[1]/div[1]/div[2]/span[1]/input[1]")
    house_number=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]"
                           "/div[1]/div[1]/div[3]/span[1]/input[1]")
    submit_button=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/input[1]")
    create_new_business=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/h4[1]")
    message_image=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/img[1]")
    private_business_company_name=(By.XPATH,"//label[contains(text(),'פרטי בית עסק')]")
    who_are_link=(By.XPATH,"//a[contains(text(),'מי אנחנו')]")
    account_link=(By.XPATH,"//a[contains(text(),'החשבון שלי')]")
    eTrado_link=(By.XPATH,"//a[contains(text(),'eTrado')]")
    contact_us_link=(By.XPATH,"//a[contains(text(),'צור קשר')]")
    payment=(By.XPATH,"//a[contains(text(),'פתרונות תשלום')]")
    MAX=(By.XPATH,"//a[contains(text(),'MAX לעסקים')]")
    card_container_but=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]")
    container_right=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]")
    how_do_i_pay=(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]")
    purchase=(By.XPATH,"//font[contains(text(),'Purchase on the website')]")














