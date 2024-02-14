# Author: Stefan DeWolfe
# Created April 2022
class DependancyChecker(object):
    def __init__(self, dependency_map):
        self.dependency_map = dependency_map

    def getDependanciesFromLibraries(self, libList):
        installStackOrder = []
        for library in libList:
            installStackOrder += self.getDependanciesFromLibrary(library)
        # needs to sort based on lowerest common node.
        return list(set(installStackOrder))

    def getDependanciesFromLibrary(self, wantedLib):
        if (wantedLib not in self.dependency_map.keys()): 
            raise Exception("Error: {} is not in the dependancy map".format(wantedLib))
        installStackOrder = []
        currentLib = wantedLib
        while (currentLib is not None):
            if(currentLib in installStackOrder): 
                raise Exception("ERROR: {} is already in dependancy map, there is a circular dependancy".format(currentLib))
            installStackOrder.insert(0,currentLib)
            currentLib = self.dependency_map.get(currentLib)
            
        return installStackOrder

def showResults(results):
        print(str(results))

def main():
    wantedLib = "GDB"
    wantedLibs = ["libelf++", "GDB"]
    dependency_map = {}
    dependency_map["Gnome 3"] = "GTK Widget Toolkit"
    dependency_map["Boost"] = None
    dependency_map["elfutils"] = "libelf++"
    dependency_map["libelf++"] = "Cairo 2D"
    dependency_map["GTK Widget Toolkit"] = "Cairo 2D"
    dependency_map["GDB"] = "elfutils"
    dependency_map["Cairo 2D"] = "Boost"
    dependency_map["Cairo"] = "ROS"
    dependency_map["Cairo 3D"] = "OpenCV"
    dependency_map["OpenCV"] = "Cairo 3D"
    dc = DependancyChecker(dependency_map)
    
    # emptyDc = DependancyChecker(dict())
    # listDc = DependancyChecker(list())
    try:
        for key in dc.dependency_map.keys():
            print(key)
            showResults(dc.getDependanciesFromLibrary(key)) 
            print("")
        print(f"{wantedLib}")
        showResults(dc.getDependanciesFromLibrary(wantedLib)) 
        showResults(dc.getDependanciesFromLibrary("Gnome")) 
        print("=================================================")
        print("")
        print(f"{wantedLibs}")
        showResults(dc.getDependanciesFromLibraries(wantedLibs)) 
        showResults(dc.getDependanciesFromLibraries(wantedLibs.reverse())) 
        print("=================================================")
        print("")
    except Exception as e:
        print(str(e))
    

main()

# ===== Summary =====

# Given a map of software package dependencies, and a request to install a piece of software, return an ordered list of all pieces of software that must be installed before the requested software can be installed.

# Assumptions you can make:

#   - Each piece of software will only ever have a single dependency
#   - There are no cyclical dependencies and you will always be able
#     to return a valid answer.
#   - Each software will only appear once as a key in the map of
#     software package dependencies


# ===== Example =====

# For the rest of this document, pieces of software will be referred to objects and their IDs, as this problem is abstractable to many different scenarios.

# The following is a map of object names, mapped to that object's dependency. For this problem, an object can only have a single dependency, but a single object can be depended on by multiple objects. Any object that has a dependency on None means that it has no dependencies.

#   == Map of Object IDs ==
#   Gnome 3,            GTK Widget Toolkit
#   Boost,              None
#   elfutils,           libelf++
#   libelf++,           Cairo 2D
#   GTK Widget Toolkit, Cairo 2D
#   GDB,                elfutils
#   Cairo 2D,           Boost

# It can be read as:
#   Gnome 3 has a dependency on GTK Widget Toolkit, 
#   Boost has no dependencies, 
#   elfutils has a dependency on libefl++, 
#   libelf++ has a dependency on Cairo 2D,
#   GTK Widget Toolkit has a dependency on Cairo 2D,
#   GDB has a dependency on elfutils,
#   Cairo 2D has a dependency on Boost

# No software appears in the left hand column more than once, each object is unique and can only have one dependency.
# A software can show up in the right hand column multiple times (a object can be depended on by multiple other objects).

# If a request came in to create object X, we need to return a list in the order that the objects should be created, such that object X was only created once all of its dependencies were also created.

# For example, if a request came in to create Gnome 3, we would need to return the following list.

# ["Boost", "Cairo 2D", "GTK Widget Tookit", "Gnome 3"]

# This list says create, in order, Boost, then Cairo 2D, then GTK Widget Toolkit, and finally, Gnome 3.

# This is because Gnome 3 depends on GTK Widget, which depends on Cairo 2D, which depends on Boost. Note that Boost does not have any dependencies so it is our final node.

# Now we can introduce the idea of a cyclical dependency. From the above example, this would be if Boost had a dependency on Gnome 3.

# If that was the case, we would not be able to return a valid order. Adjust your solution so that it detects this case and returns an error alerting the requestor to this.
#=============================================================================
# For the Third part of the question, use this example for requesting multiple objects at once, in this example we are asking for objects Gnome 3 and libelf++.

# [Boost, Cairo 2D, GTK Widget Toolkit, Gnome 3, libelf++] would be a correct solution.
# [Boost, Cairo 2D, libelf++, GTK Widget Toolkit, Gnome 3] would also be a correct solution.
#=============================================================================
# Gnome 3 and libelf++ share two dependencies, Cairo 2D, and Boost, but beyond that, they are independent so the ordering of the other installers doesn't matter once their common dependencies are installed.
