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

##### CHAPTER 5 - rebase, amend, and cherry-pick #####

# git rebase 主分支 - 通常是由於功能分支在基於 main 分出來時，main 這邊被更新了導致有新版本的 main，當功能分支要 merge 回 main 時，
#                     git 會自動建立一個新的 commit 分別指向最新的 main 和最新的功能分支，因此太多次這種情況會導致很多不重要的 commit 資訊
#                     此時就能用 rebase 功能，讓功能分支的"最舊版本"接上 main 的最新版本
# git reset ORIG_HEAD -hard - 復原到 rebase 前的狀態


# test --amend command

# git cherry-pick 需要的 commit ID - 不全部 commit 而是選擇特定要 commit 的版本