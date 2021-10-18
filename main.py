import sys, time, shutil, datetime

print("NonQueror Command Line Interface v1.1.0")

def _add(f, c):
    with open(f, "w") as f:
        f.write(c)
        f.close()

def main(args):
    if args[0] == "create":
        __import__(args[1]).create((args[2] if len(args) > 2 else "."))
    if args[0] == "build":
        input("This might overwrite some files. Continue by hitting enter key, cancel by pressing CMD+C. ")
        __import__(args[1]).build((args[2] if len(args) > 2 else "."))
    if args[0] == "run":
        __import__(args[1]).run((args[2] if len(args) > 2 else "."))
    if args[0] == "add":
        __import__(args[1]).add(args[2],(args[3] if len(args) > 3 else "."))
    if args[0] == "backup":
        print("Building backup...")
        filename = datetime.datetime.now().strftime("Backup-%m-%d-%Y-%H-%M-%S")
        shutil.make_archive(filename, 'zip', (args[1] if len(args) > 2 else "."))
        print("Done. Move "+filename+" to another hard drive for more safety.")

if __name__ == "__main__":
    start = time.time()
    main(sys.argv[1:])
    print("Finished in "+str(round(float(time.time() - start),3))+" seconds.")
    print("Operation completed successfully.")