
import tarfile
import glob


def create_tar():
  tfile = tarfile.open("mytarfile2.tar", "w")

  for each in glob.glob("/Users/petre/Desktop/*.pdf"):
    tfile.add(each)

  tfile.close()

create_tar()
