# LaTeX Source

This directory contains an uncompressed copy of the source uploaded to arXiv
for ease-of-inspection.

An additional copy of the paper is also available here in the
[`hayesall_srlearn.pdf`](https://github.com/hayesall/srlearn-StarAI-2020-workshop/blob/master/paper/hayesall_srlearn.pdf)
file.

## Building the document

This assumes you have a LaTeX distribution installed locally, and access to
a UNIX-like environment.

### Prerequisites

- PDFLaTeX (`pdflatex --version`)

### Building

Run `pdflatex` twice to build the document and the references (minted listings
and bibliography references should not need to be built in this version).

```bash
$ pdflatex hayesall_srlearn
$ pdflatex hayesall_srlearn
```
