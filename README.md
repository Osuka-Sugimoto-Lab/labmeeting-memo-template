## 2018/1/11 naniwa
スタートダッシュを終えてから読んで使ってください．
まずは一度，template.texのタイプセット(pdf化)を行いましょう．
(ここでうまくpdf化できない人はtexのセットアップからやり直し)
そしてpdf化したtemplate.pdfとtemplate.texの中身を見比べながら読み進めましょう．

中身を十分理解できたという人は，
「template.texではなく，template_blank.texにあなたの資料を書き込みましょう」
template.texはできればそのままにしておいて，template_blank.texはmain.texでもなんでも
好きな名前に変えて使ってください．

向上心のある方はosukalab2018.styの中身や，referenceフォルダの中にある
各種パッケージのリファレンスを読むと，いろんな自由度が高くなるでしょう．

## 2020/9/30 naniwa

template.texをタイプセットした時にいくつか警告が出ますが，
そのうちcaptionパッケージに関わるものは無視して大丈夫です．

Unsupported document class (or package) detected,
(caption)	usage of the caption package is not recommended.
See the caption package documentation for explanation.

こういうの．
これはcaptionパッケージが研究会資料のドキュメントスタイルに明示的に対応していないことを警告しており，
実際の使用上では問題がない（とおもわれる）ため無視して良いということです．
よしなに

## 2021/1/29 naniwa

ドキュメントクラスをニューノーマルなjlreqに．
それに合わせて詳細を変更．
あと上記変更に伴って，\bfとか\itは完全に使えなくなりました．

参考： [日本語 LaTeX の新常識 2021](https://qiita.com/wtsnjp/items/76557b1598445a1fc9da)
