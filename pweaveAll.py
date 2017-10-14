#!/usr/bin/env python3
import os
from pweave import Pweb, PwebTexPweaveFormatter


filenames = [
    "expdistribution",
    "constructiondiscretetime",
    "constructioncontinuoustime",
    "random_walk",
    "ratestability",
    "empericalperfmeasures",
    "levelcrossing",
    "ratestability",
    "mm1",
    "mnmn1",
    "pasta",
    "little",
    "usefulidentities",
    "mg1",
    "batcharrivals",
    "mg1distributionqueuelength",
    "mg1density",
    "gg1",
    "serviceInterruptions",
    "process_batches",
    "tandem",
    "convolution",
    "mva",
    "mda",
]

# to select some files temporarily

filenames = [
    #"little",
    #"usefulidentities",
    #"mg1",
    #"batcharrivals",
    #"mg1distributionqueuelength",
    #"gg1",
    #"serviceInterruptions",
    "process_batches",
        ]


current_dir = os.path.dirname(os.path.realpath(__file__))
chunk_dir = current_dir + "/chunks/"
tex_dir = current_dir + "/tex_files/"


class ToFile(PwebTexPweaveFormatter):
    chunks = []

    def preformat_chunk(self, chunk):
        ToFile.chunks.append(chunk.copy())  # Store the chunks
        if chunk['type'] == 'code':
            source = os.path.basename(self.source)
            source = os.path.splitext(source)[0]
            fname = chunk_dir + "{}_{}.tex".format(source, chunk['number'])
            with open(fname, "w") as f:
                if chunk['term']:
                    f.write(chunk['result'])
                    chunk['result'] = r"\lstinputlisting{"+fname+"}"
                else:
                    f.write(chunk['content'])
                    f.write(chunk['result'])
                    chunk['content'] = r"\lstinputlisting{"+fname+"}"
                    chunk['result'] = "\n\n"
        print(chunk)
        return(chunk)


for fname in filenames:
    #doc = Pweb(tex_dir + fname+r".tex", format="texpweave",
    doc = Pweb(tex_dir + fname+r".tex", informat="noweb",
               doctype="tex", 
               output=chunk_dir+fname+r".tx")
    
    # doc.setformat(Formatter=ToFile)
#     doc.updateformat({
#         "outputstart": "\n",
#         "outputend": "\n",
#         "codestart": "\n",
#         "codeend": "\n",
#         "termstart": "\n",
#         "termend": "\n",
#     }
#     )
    doc.updateformat({
        "outputstart": r"\begin{lstlisting}",
        "outputend": r"\end{lstlisting}",
        "codestart": r"\begin{lstlisting}",
        "codeend": r"\end{lstlisting}",
        "termstart": r"\begin{lstlisting}",
        "termend": r"\end{lstlisting}",
    }
    )
    #print(doc.getformat())
    doc.weave()
