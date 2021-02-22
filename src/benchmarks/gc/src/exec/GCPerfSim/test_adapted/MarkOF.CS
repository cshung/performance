using System;
using System.Collections.Generic;

// The purpose of this is to test the BGC mark stack overflow code path which is rarely hit.
// We create an object graph that contains a very long path which consists of many nodes.
// you can specify the # of nodes you want in the constructor of the MarkOF class. 
// The fields of this class is intentionally laid out this way to maximize the mark stack space
// it uses without consuming much heap space so it can hit overflow easily.
namespace testMarkOF
{
    class NoRefType
    {
        int _i;
        int _j;
        public NoRefType(int i, int j)
        {
            _i = i;
            _j = j;
        }
    }
    class RType
    {
        NoRefType noRef0;
        NoRefType noRef1;

        public RType(int i)
        {
            i *= 10;
            noRef0 = new NoRefType(i + 1, i + 2);
            noRef1 = new NoRefType(i + 3, i + 4);
        }
    }

    // The idea of the MarkOF class is it needs to create a very long path in the object graph.
    // And it does this by recursively creating as many as nodes on that path as requested.
    class MarkOF
    {
        public int level;
        public RType r0;
        public RType r1;
        public RType r2;
        public RType r3;
        public RType r4;
        public RType r5;
        public RType r6;
        public RType r7;
        public MarkOF objToRecurseEnd;

        public MarkOF(int numNodesToCreate)
        {
            level = numNodesToCreate;
            Populate();
        }

        void Populate()
        {
            r0 = new RType(level);
            r1 = new RType(level);
            r2 = new RType(level);
            r3 = new RType(level);
            r4 = new RType(level);
            r5 = new RType(level);
            r6 = new RType(level);
            r7 = new RType(level);

            level--;
            if (level > 0)
            {
                objToRecurseEnd = new MarkOF(level);
                //Console.WriteLine("creating a lower level {0} obj", level);
            }
        }
    }

    class Program
    {
        // 4Gb of unused
        private static byte[] unused1 = new byte[1024 * 1024 * 1024];
        private static byte[] unused2 = new byte[1024 * 1024 * 1024];
        private static byte[] unused3 = new byte[1024 * 1024 * 1024];
        private static byte[] unused4 = new byte[1024 * 1024 * 1024];

        static List<object> list;
        static MarkOF last;
        static void Allocate(int sizeInMB)
        {
            list = new List<object>();
            ulong allocated = 0;
            while (allocated < ((ulong)sizeInMB * 1024 * 1024))
            {
                byte[] b = new byte[8 * 1024];
                list.Add(b);
                allocated += 8 * 1024 + 24;
            }
        }
        public static int Bing(string[] args)
        {
            unused1[0] = 0;
            unused2[0] = 0;
            unused3[0] = 0;
            unused4[0] = 0;

            bool fInStress = false;
            int level = 150;
            if (args.Length > 0)
            {
                if (args[0].ToLower() == "stress")
                    fInStress = true;
            }

            for (int i = 0; i < 4; i++)
            {
                list = null;
                // If we are running this standalone we need a heap that's not too small or
                // we will never do BGCs.
                // For running in stress however, since other tests will be creating plenty
                // of memory we just allocate a small amount here.
                Allocate(fInStress ? 1 : 100);

                // Console.WriteLine("creating {0} levels", level);

                level *= 2;
                MarkOF objMarkOF = new MarkOF(level);
                last = objMarkOF;
                // For running standalone this induced GC can show mark overflow.
                // When running in stress BGCs will already be naturally triggered.
                if (!fInStress)
                {
                    GC.Collect(2, GCCollectionMode.Default, false, false);
                }
                if (list != null)
                {
                    // Console.WriteLine("list has {0} elements", list.Count);
                }

                // Console.WriteLine("heap size is {0} bytes, OF obj has {1} levels", GC.GetTotalMemory(false), objMarkOF.level);
            }

            return 100;
        }
    }
}
