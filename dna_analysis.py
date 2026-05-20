dna = "ATGCGTAGCTA"

print("DNA Sequence:", dna)
print("Length:", len(dna))
print("A Count:", dna.count("A"))
print("T Count:", dna.count("T"))
print("G Count:", dna.count("G"))
print("C Count:", dna.count("c"))

gc_content=((dna.count("G") + dna.count("C")) / len(dna)) * 100

print("GC content:", round(gc-content, 2), "%")
