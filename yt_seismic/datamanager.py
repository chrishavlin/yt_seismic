import os

class filesysDB(object):
    def __init__(self,top_level_dir=None):
        """
        simple file system database manager

        Parameters
        ----------
        top_level_dir   the top level directory to search for data files. If
                        None, will check for environment variable YTVELMODELDIR
        """
        if top_level_dir is None:
            top_level_dir = os.environ.get('YTVELMODELDIR')

        self.db_path=top_level_dir
        self.buildFileDictionary()
        return

    def buildFileDictionary(self):
        """builds dictionaries of available files

        Returns
        -------
        None


        """
        self.FileDict = {}
        self.FilesByDir = {
            'IRIS_models':[],
            'IRIS_refModels':[],
            'shapedata':[]
        }
        for root, subdirs, files in os.walk(self.db_path):
            fileList=files # files in this root
            for file in files:
                full_fi=os.path.join(root,file)
                self.FileDict[file]=full_fi
                for dirname in self.FilesByDir.keys():
                    if dirname in full_fi:
                        self.FilesByDir[dirname].append(file)
        return

    def validateFile(self,fname):
        """ checks if file exists

        Returns
        -------
        str or bool
            returns the filename if it exists, False if not
        """
        validFile=False
        if os.path.isfile(fname):
            validFile=fname
        else:
            if fname in self.FileDict.keys():
                validFile=self.FileDict[fname]

        return validFile
