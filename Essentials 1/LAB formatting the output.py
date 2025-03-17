

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


#minimize the number of print() function invocations by inserting the \n sequence into the strings;
#make the arrow twice as large (but keep the proportions)
#duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
#remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error ‒ is this the place where the error really exists?
#do the same with some of the parentheses;
#change any of the print words into something else, differing only in case (e.g., Print) ‒ what happens now?
#replace some of the quotes with apostrophes; watch what happens carefully.


print("     *", "     *", sep="      ")
print("    * *", "    * *", sep="     ")
print("   *   *", "   *   *", sep="    ")
print("  *     *", "  *     *", sep="   ")
print(" *       *", " *       *", sep="  ")
print("***     ***", "***     ***", sep=" ")
print("  *     *", "  *     *\n  *     *", "  *     *", sep="   ")
print("  *******", "  *******", sep="   ")
