# TODO 紀錄指令

# git clone https://github.com/用戶名稱/雲端儲存庫名稱 - 在本地端建立一個儲存庫，儲存庫的內容由雲端儲存庫複製而來，兩者建立連結
# git init - 直接在本機端建立儲存庫做版控，之後可透過其他方式上傳到 Github


# git statul - 查看狀態

# git add 資料夾路徑 or git add . - 請 Git 追蹤此資料夾，此後檔案的狀態將存入 staging area 整備區

# [Note] 一定要 add + commit 兩步驟才是正式紀錄到儲存庫，add 只是暫存
# git commit - 送出 commit 即是將當前資料夾內容創造出一個checkpoint，也等於一個版本
    # -m "此 commit 的說明訊息"
    # -a 跳過整備區階段，直接送出 commit，需在 -m 之前
    # --amend 在未 push 前，修改上一次 commit 的訊息

# git push - 將本機儲存庫的改變同步到雲端儲存庫

# add this message from second local repository

# git log - 查看 commit 紀錄
    # --oneline - 單行顯示

##### CHAPTER 3 - Branch #####

# Branch (分支) - 當要處理 bug 或開發新功能時，建立一個新分支(aka feature branch)，此分支是當前最新版本的副本
# Key Concept - branch 上的更動先 merge 回 main，再由主分支 main 去 push，易於管控也確保主分支是乾淨的，

# git barnch 分支名稱 - 建立分支
# git checkout 分支名稱 - 切換到分支的名稱(checkout "to")
# git checkout -b 分支名稱 - 建立 + 切換
# git push --set-upstream origin 分支名稱 - 當新建立的分支還沒被雲端儲存庫認識前使用，僅第一次需要，用過後就跟一般 push 一樣
# git merge 分支名稱 - 將分支 merge 回來(ex: 在分支 B 修改後，想將 B merge 回 A，則先 git checkout A + git merge B)

# add to test KDiff3 from branch Calculator

##### CHAPTER 4 - 檢視 commits 內容並 merge 分支 #####
# git show - 顯示 1.作者 2.日期 3.commit msg 4.和前一個 commit 版本的差異(a:前一個, b:當前新曾)


##### CHAPTER 5 - rebase, amend, and cherry-pick #####

# git rebase 主分支 - 通常是由於功能分支在基於 main 分出來時，main 這邊被更新了導致有新版本的 main，當功能分支要 merge 回 main 時，
#                     git 會自動建立一個新的 commit 分別指向最新的 main 和最新的功能分支，因此太多次這種情況會導致很多不重要的 commit 資訊
#                     此時就能用 rebase 功能，讓功能分支的"最舊版本"接上 main 的最新版本
# git reset ORIG_HEAD -hard - 復原到 rebase 前的狀態


# test --amend command

# git cherry-pick 需要的 commit ID - 不全部 commit 而是選擇特定要 commit 的版本

##### CHAPTER 6 - 用 Interactive rebase 修改 commit 歷史紀錄 #####

# git rebase -i - 啟動 Interactive rebase
# git rebase -i HEAD~7 顯示最新的 7 個 commit
# 進入 Interactive rebase 後，將 pick 改為 s 代表將其壓縮至前一個 commit

##### CHAPTER 7 - 製作儲存庫副本 (mirror)、notes 與 tag 等實用指令 #####

# git push --mirror "url of repos2" - 建立一個完全一樣(連檔案建立時間都一樣)的副本到另一個 repository
#                                     commitID、commit、HEAD、origin 都和原本的一樣，之後可以任意更改不會影響到另一個

# git note add -m "attached message" commitID - 為指定的 commit 附加新的訊息，常用在 1.新增資訊 2.單純標記(maybe for 後續 rebase) 
#                                               3.描述 commit 之間的關係，之後用 log 去看會多出 Notes 訊息
#                                                   
# git tag 標籤名稱 commitID - 簡單標籤：為一個 commit 建立標籤，非常顯眼，可用來標記重要版本，這樣就能看到版本跟版本間做了哪些 commit
# git tag 標籤名稱 commitID -m "註解訊息" - 帶註解標籤：要用 git show 標籤名稱，才看得出差別
# git tag -f 標籤名稱 new_commitID - 如果標籤給錯，重新下給新的 commitID
# git tag -d 標籤名稱 - 刪除標籤