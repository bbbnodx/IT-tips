# Windows10 PC セットアップ手順
この文書はAI推進室において、WinPCを開発機としてセットアップするための手順を備忘録的にまとめたものです。

- [1. KSK標準初期設定手順](#1-KSK標準初期設定手順)
  - [1.1 不要なプリインストールソフトウェアのアンインストール](#11-不要なプリインストールソフトウェアのアンインストール)
  - [1.2 McAfeeのインストール](#12-McAfeeのインストール)
  - [1.3 McAfeeの更新とウイルススキャン](#13-McAfeeの更新とウイルススキャン)
  - [1.4 Microsoft Office(32bit)のインストール](#14-Microsoft-Office32bitのインストール)
  - [1.5 Windows Updateの実行](#15-Windows-Updateの実行)
  - [1.6 ISMCクライアントのインストール](#16-ISMCクライアントのインストール)
  - [1.7 その他必要ソフトウェアのインストール](#17-その他必要ソフトウェアのインストール)
  - [1.8 新宿GC複合機ドライバのインストール](#18-新宿GC複合機ドライバのインストール)
- [2. 開発環境の構築](#2-開発環境の構築)
  - [2.1 Anacondaのインストール](#21-Anacondaのインストール)
  - [2.2 VS Codeのインストール](#22-VS-Codeのインストール)
  - [2.3 Gitのインストール](#23-Gitのインストール)
  - [2.4 Microsoft Build Tools for Visual Studioのインストール](#24-Microsoft-Build-Tools-for-Visual-Studioのインストール)
  - [2.5 NVIDIAドライバアップデート](#25-NVIDIAドライバアップデート)
  - [2.6 CUDAのインストール](#26-CUDAのインストール)
  - [2.7 cuDNNのインストール](#27-cuDNNのインストール)
- [3. Deep Learning フレームワークの構築](#3-Deep-Learning-フレームワークの構築)
  - [3.1 Tensorflow + Keras](#31-Tensorflow--Keras)
  - [3.2 Chainer](#32-Chainer)
  - [3.3 PyTorch](#33-PyTorch)
  - [3.4 Sony NNC(Windows版)](#34-Sony-NNCWindows版)
  - [3.5 Sony NNabla](#35-Sony-NNabla)
- [4. Anaconda仮想環境の使い方](#4-Anaconda仮想環境の使い方)
  - [4.1 ターミナルの初期設定](#41-ターミナルの初期設定)
    - [2019/6/11追記](#2019611追記)
  - [4.2 仮想環境の作成と切り替え](#42-仮想環境の作成と切り替え)
  - [4.3 パッケージのインストール](#43-パッケージのインストール)
  - [4.4 仮想環境の削除](#44-仮想環境の削除)
  - [4.3 VS Codeの設定](#43-VS-Codeの設定)

## 1. KSK標準初期設定手順
最初はCOMPASSの[PC設定手順(社内)](http://compass.ksk.local/compass/main/pc_setting.pdf)に則ってセットアップします。  
なお、KSK-LANに接続するWindows機を想定しているため、COMPASSのリンクは全て社内リンクです。

### 1.1 不要なプリインストールソフトウェアのアンインストール
Windowsの初期設定が終わったら、まず不要なプリインストールソフトウェアをアンインストールしてください。**特に、McAfeeは必ずアンインストールしてください**。既存のMcAfeeが存在すると、KSK標準のMcAfeeソフトウェアのインストールに失敗します。

### 1.2 McAfeeのインストール
「McAfeeエージェント」と「McAfee VirusScan Enterprise」をインストールする必要があります。COMPASSの[VirusScan(社内)](http://compass.ksk.local/compass/main/jyouhoutotejyun/software/virusscan.html)から必要ファイルをダウンロードし、手順に沿ってインストールしてください。なお、**この作業はWindows Updateをかける前に行うことが推奨されています**(COMPASS参照)。

### 1.3 McAfeeの更新とウイルススキャン
McAfeeのインストールが完了したら、定義ファイルを更新してフルスキャンを実行してください。

### 1.4 Microsoft Office(32bit)のインストール
Officeは本来はAXISに申請し、承認を得てからインストールしますが、慣例的に先行インストールができます。OfficeのバイナリはDirectCloud-Boxに置かれています(2019/3/7現在)。ライセンスキーも同じディレクトリに置かれているので、認証を済ませてください。  
また、池田GMにOfficeのインストール申請を出してください。

### 1.5 Windows Updateの実行
Windows Updateを実行してください。複数回実行が必要なこともあります。

### 1.6 ISMCクライアントのインストール
まず、資産番号シールを貼り付けていることを確認してください。まだの場合は、速やかに貼り付けてください。ISMCクライアントはCOMPASSの[IT資産管理ツール(社内)](http://compass.ksk.local/compass/main/jyouhoutotejyun/software/itsisan-kanri-tool.html)で配布されています。設定手順も公開されているので、確認しながら設定してください。  
また、"\\\\ADP2\\管理共有\\06セキュリティ\\17ISMS\\30_管理台帳\\19_13.ハードウェア管理台帳\\ハードウェア管理台帳.xlsx"にPCの情報を追記してください。

### 1.7 その他必要ソフトウェアのインストール
その他に必要なソフトウェアをCOMPASSの[ソフトウェア一覧](http://compass.ksk.local/compass/main/Software.pdf)からインストールしてください。少なくともAdobe ReaderとGoogle Chromeは必要かと思います。

### 1.8 新宿GC複合機ドライバのインストール
"\\\\ADP2\\管理共有\\24共有ツール\\新宿GC_新複合機\\19新宿GC3F　FFBUドライバ\\"から複合機のドライバをコピーし、インストールしてください。

追記：Windows10環境ではTCP/IP接続で印刷できない不具合(?)が報告されています。その場合はプリンタのプロパティを開き、ポートからWSD Portにチェックを入れてください。

追記その2：[コントロールパネル] > [デバイスとプリンタ]でネットワークからプリンタを探して設定した方が確実です。


## 2. 開発環境の構築
まず事前に"\\\\ADP2\\管理共有\\06セキュリティ\\17ISMS\\30_管理台帳\\19_12.ソフトウェア管理台帳\\フリーソフトウェア管理台帳(AI).xlsx"を参照し、インストールしようとするソフトウェアが許可済みであるかどうか確認してください。  
ただし、次に該当するものは原則として台帳に記載がなくてもインストールできます：
- NVIDIAのドライバソフトウェア(ハードウェアに紐づくため)
- Pythonのパッケージ(Pythonの許可で承認済みと解釈)
- エディタの拡張機能(エディタの許可で承認済みと解釈)

当たり前ですが、業務に不要なものはインストールしないでください。

### 2.1 Anacondaのインストール
[Anaconda Distribution](https://www.anaconda.com/distribution/)

公式ページからPython3系の最新ディストリビューションをダウンロードしてインストールしてください。インストール設定の途中で環境変数の設定が非推奨(Not recommended)になっていますが、その場合Anaconda promptというターミナルでしかPythonにアクセスできません。Windowsの場合はさほど影響もないので、環境変数に設定してしまっても構いません。一応、curlなどがAnaconda環境優先になってしまうことに留意しておきましょう。  
Anacondaの注意点として、パッケージの管理がpipではなくcondaになります。pipも使えますが、Anaconda環境でpipを使うと不具合が起こるという報告が少なからずありますので、可能な限りconda経由でパッケージをインストールしてください。  

Pythonパッケージをインストールするときは、原則として仮想環境を使います。詳しくは[4. Anaconda仮想環境の使い方](#4-anaconda仮想環境の使い方)を参照してください。


### 2.2 VS Codeのインストール
[Visual Studio Code - Microsoft](https://code.visualstudio.com/)

VS CodeはMicrosoftのIDE(統合開発環境)であるVisual Studioを軽量化した開発用エディタで、無料で利用することができます。AI推進室の標準エディタとなっているので、特に理由がなければVS Codeで開発してください。

VS Code拡張、設定などは**職業倫理に反しない範囲で**自由に設定できます。  
AI推進室の標準設定が[KSK-AIのVS Code設定](https://github.com/ksk-ai/AI_StandardDevConf/blob/master/KSKSettingForVSCode.md)にまとめられているので、参照してください。

上記リンクに記載されていない部分について：  
最低でも次の拡張はインストールしましょう。
- Python (Microsoft)
- Japanese Language Pack for Visual Studio Code


Git Bash(または任意のシェル)を統合ターミナルとして用いたい時は、settings.jsonを開いて以下の記述を追記します(パスは適宜置き換えてください)：
```json
"terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe"
```


### 2.3 Gitのインストール
[Git for Windows](https://gitforwindows.org/)

バイナリをダウンロードして実行すると、Git環境とGitBashがインストールされます。  
インストール設定は基本的にデフォルトでいいはずですが、"Configuring the line ending conversions"(改行コードの設定)だけは「Checkout as-is, commit as-is」(何もしない)としてください。  
Windowsの改行コードはCRLFで、UNIX系のOSはLFです。Git側で改行コードを自動変換してくれるように設定できますが、トラブルの元なので何もしないように設定するのが無難です。改行コードはエディタ側で設定しましょう。

GitHubアカウントが既にある場合は、configにアカウントの情報を追記しましょう。
```bash
$ git config --global user.name "アカウント名"
$ git config --global user.email "メールアドレス"

# 反映されているか確認
$ cat ~/.gitconfig

[user]
    name = アカウント名
    email = メールアドレス
```


### 2.4 Microsoft Build Tools for Visual Studioのインストール
Windowsは他のOSと異なり、標準のCコンパイラを持っていません。一部のソフトウェアやパッケージはソースコードからのビルドが必要になることもあるので、ビルドツールをインストールします。  
[Visual Studio 2019](https://www.visualstudio.microsoft.com/downloads/)のページ下部から「Tools for Visual Studio 2019」を開いて「Build Tools for Visual Studio 2019」をダウンロードしてください。  
インストール画面でワークロードの「Visual C++ Build Tools」を選択し、インストールします。~~Cupyをインストールしたい場合は、「デスクトップ用のVC++2015.3 v140ツールセット」にもチェックを入れます。Cupyのインストールはやや面倒なので、後述の資料を参考にしてください。~~ 最新版のBuild Toolsでインストールできるようになりました。

### 2.5 NVIDIAドライバアップデート
デフォルトでNVIDIA GeForce Experienceがインストールされているので、NVIDIAアカウントでログインすればアップデートできます。手間を惜しまないのであれば、手動でNVIDIAのサイトからダウンロードしてきても大丈夫です。

### 2.6 CUDAのインストール
[NVIDIA CUDA](https://developer.nvidia.com/cuda-downloads)

最新版は深層学習ライブラリが対応していないこともあるので、ライブラリのドキュメントを確認してからバージョンを選んでください。特にNNablaはマイナーなのでCUDAの対応が遅いです。

### 2.7 cuDNNのインストール
[NVIDIA cuDNN](https://developer.nvidia.com/cudnn) (要NVIDIAアカウント登録)

cuDNNをダウンロードするにはNVIDIAアカウントでサインインする必要があります。  
CUDAほどバージョンに厳密ではないので、基本的には最新版を使えば大丈夫ですが、CUDAのバージョンには合わせる必要があります。



## 3. Deep Learning フレームワークの構築
各フレームワークはOSとCUDAのバージョンの違いによってインストール手順が変わります。公式ページを注意深く読んで、適切な手順でインストールしてください。特にWindowsは疎外され気味です。

基本的にAnacondaで仮想環境を作り、その中にインストールします。
```bash
$ conda create -n NewEnv
$ conda activate NewEnv
```

作成した仮想環境は以下のコマンドで確認できます。
```bash
$ conda info -e
# conda environments:
#
base                C:\Users\USERNAME\Anaconda3
NewEnv          *   C:\Users\USERNAME\Abacibda3\envs\NewEnv
```



### 3.1 Tensorflow + Keras
[TensorFlow | GPU support](https://www.tensorflow.org/install/gpu)


公式ページの手順に従ってインストールします。GPU対応パッケージは`tensorflow-gpu`であることに注意してください。リンク先ページの最下部にあるように、環境変数を追加する必要もあります。  

### 3.2 Chainer
[Chainer documentation - Installation](https://docs.chainer.org/en/stable/install.html)

公式にはUbuntuとCentOSのみが推奨環境であり、MacとWindowsを含む他のOSでの動作は保証しないと書かれています。

```bash
$ pip install chainer
```
ChainerでGPUを活用するには、別途Cupyというライブラリをインストールする必要があります。  
CupyはNumpyの主要なクラス、メソッドをGPUで計算するためのライブラリです。ただし、完全互換ではありません。元々はChainerの一部でしたが、現在は分離して提供されるようになりました。Chainerを用いない場合でも、NumPy配列計算を高速化したい場合には便利です。  
  

~~最新版のCupyをインストールするには、やや面倒な手順が必要です。~~  
Cupy6.0.0 以降では、比較的簡単になりました。
1. Visual Studio Build Tools 2019をインストール([2.4節](#24-Microsoft-Build-Toolsのインストール)を参照)  
2. pipでCupyをインストール(CUDAのバージョンによって変わるので注意)
```bash
$ pip install cupy-cuda100
```


### 3.3 PyTorch
[PyTorch | Get Started](https://pytorch.org/get-started/locally/)

上記ページで自分の環境をクリックして選択すれば、`torch`と`torchvision`のインストール方法が表示されます。CUDAインストール済みの環境ではpip経由インストール、CUDAが入っていないもしくは別バージョンのCUDAを使いたい場合はconda経由インストールを推奨します。

### 3.4 Sony NNC(Windows版)
[公式サイト](https://dl.sony.com/ja/app/)でメールアドレスを登録し、届いたメールのリンクからアーカイブをダウンロードできます。ただし、あまりマイナーアップデートされないようなので、ADP1に置かれているアーカイブからインストールしても良いでしょう。  

アーカイブをSSDドライブの適当な場所に展開してください。一般的には「`C:\Users\USERNAME\`」または「`C:\Users\USERNAME\tools\`」にしておけばいいと思います。  
初回起動時に「Visual Studio 2015のVisual C++ 再頒布可能パッケージがインストールされていません」という旨の警告が表示されますが、「Microsoft Visual C++ 2017 Redistributable」がインスールされていれば問題ありません。むしろ、その状態だと2015パッケージはインストールできません。  
[ENGINE]の設定で[GPU], [Default]に変更し、GPUが使えることを確認してください。

### 3.5 Sony NNabla
[NNabla package installation using PIP](https://nnabla.readthedocs.io/en/latest/python/pip_installation.html)  
[NNabla CUDA extension package installation using PIP](https://nnabla.readthedocs.io/en/latest/python/pip_installation_cuda.html)
```bash
$ pip install nnabla
$ pip install nnabla-ext-cuda100  # CUDA10.0
$ pip install pywin32  # Windows環境の場合は必須
```


## 4. Anaconda仮想環境の使い方
プロジェクトによってはPythonやパッケージのバージョン指定が必要な場合があります。  
そういう場合には仮想環境を利用すると、プロジェクト単位の環境を作成できて便利です。  
また、condaとpipの競合問題から安全を確保するためにも、Anaconda環境にパッケージを追加するときは基本的に仮想環境で行うと良いでしょう。  
ちなみに、仮想環境は`~/Anaconda3/envs/`以下に作成されます(Anacondaのインストール先を変更していたら適宜読み替えてください)。

### 4.1 ターミナルの初期設定
仮想環境の利用を始める前に、ターミナルの初期設定を済ませる必要があります。
```powershell
> conda init
```
ターミナル環境としてbashを利用しているときは、事前に`.bashrc`を作成する必要があります。
```bash
$ touch ~/.bashrc  # .bashrcが存在しないときは空ファイルを作成
$ conda init bash
```
ターミナルの初期設定が済むと、プロンプトに現在のAnaconda環境が表示されるようになります。デフォルトはbaseです。
```bash
(base)
$ 
```

#### 2019/6/11追記
現在のcondaのバージョンでは、`.bashrc`ではなく`.bash_profile`にコードを追加します。私の環境では上手く動かなかったので、`.bash_profile`に書き込まれたコードを`.bashrc`に移して動作するようになりました。

### 4.2 仮想環境の作成と切り替え
以下のコマンドで新しい環境`new_env`を作成します。Pythonのバージョン指定がないときは、インストール可能な最新バージョンで作成されます。
```bash
(base)
$ conda create -n new_env python=3.6
```
Anacondaのbase環境から指定したパッケージを引き継ぐことが可能です。
```bash
(base)
$ conda create -n new_env python=3.6 anaconda
```
仮想環境の切り替えには`conda activate`を使います。また、`conda deactivate`で仮想環境から抜けます。
```bash
(base)
$ conda activate new_env
(new_env)
$ conda deactivate
```
以下のコマンドで仮想環境一覧を参照できます。
```bash
(base)
$ conda info -e
# conda environments:
#
base                  *  C:\Users\02\Anaconda3
ai-ocr                   C:\Users\02\Anaconda3\envs\ai-ocr
new_env                  C:\Users\02\Anaconda3\envs\new_env
```

### 4.3 パッケージのインストール
仮想環境に入ってpipかcondaでインストールするだけです。
```bash
(base)
$ conda activate new_env
(new_env)
$ pip install numpy
```

注意点として、Jupyterやipythonのようにターミナルから実行するパッケージは、仮想環境にインストールされていないときはbase環境のパッケージが実行されます。そのときはactivateに関係なくbase環境が参照されます。  



### 4.4 仮想環境の削除
不要な仮想環境は削除できます。
```bash
(new_env)
$ conda deactivate
(base)
$ conda remove -n new_env --all
(base)
$ conda info -e
# conda environments:
#
base                  *  C:\Users\02\Anaconda3
ai-ocr                   C:\Users\02\Anaconda3\envs\ai-ocr
```

### 4.3 VS Codeの設定
VS Code側でも使用する環境に合わせてパスを設定しないと、linterが正しく動作しません。  
`python.condaPath`を正しく設定していると、Pythonファイルを開いているときウィンドウ最下部のステータスバーに`Python 3.6.8 64-bit ('base': conda)`という表記が出ます。それをクリックすると一覧から仮想環境を選択できます。こうすると、`.vscode/settings.json`に次の設定が書き込まれます。
```json
{
    "python.pythonPath": "C:\\Users\\USER_NAME\\Anaconda3\\envs\\ENV_NAME\\python.exe",
}
```

手動で変更したい場合は、コマンドパレットから`Preferrences: Open Workspace Settings`を開いて編集します。
