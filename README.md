# Python DesignPatterns
## 1. 監聽模式
### introduction
1. 監聽模式，又稱為觀察者模式
2. 監聽模式有以下特點 :   
    i. 一個物件的狀態或資料的更新，需要仰賴其他物件同步更新，或者一個物件的更新需要依賴另外一個物件更新  
    ii. 物件僅需要將自己的更新推送給其他物件，而不需要知道其他物件的細節
3. 設計重點:
    1. 要明確定義誰是觀察者(監聽物件)，誰是被觀察者，只要確定誰是應該被關注的物件，問題也就明白了；觀察者和被觀察者是多對一的關係，如一個網頁的輸入方框，會有滑鼠點擊的監聽者、也有鍵盤的監聽者
    2. 被觀察者至少需要有三個方法: 1.新增觀察者(監聽者) 2.移除監聽者 3.通知監聽者
4. 舉例 : 消息推播

## 2. 狀態模式
### introduction
1. 允許一個物件，在其狀態發生改變時，同時改變他的行為



https://atp_cert_storage.storage.googleapis.com/20230830_marketing_gke_1_day/Zong_Yao_Yang.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=course-complete-cert-sc%40tw-rd-trainer-jason.iam.gserviceaccount.com%2F20230904%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230904T022650Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&x-goog-signature=6da3e4b18ea8a4220dae175f972a352d7eaa28018de69996043c79d7c51cfd5059ea9507dd66be48f6f228b1eb4cc26b02a715003cfe23bda64ba829071c4f8bcb41d45a0846654793fb0b2c5c883b9e7fc7d7bb3b6db4c38deebc92c1de432dedcc1e648e798950e78b04605fceb7401647aa8bd1f2f5fcd16a5627e73138b3f170f96f1b695ac928e9b959e9b788d13b509874ab2579adb0ec911a596207014496133e409ab0df8fb70de3be6c695915051d89be20ee358ebf30907adbbcaba87841aacec764bd3e0d5ab168d960767927899f879c43fdcfcad883afa33a60a82f6e47855415eb26569bcdf9406800e26926101984207bea857024c81fc82d