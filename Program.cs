namespace Prisoner
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int universe = 1;
            int success = 0;
            int failure = 0;
            for (int i = 0; i < 10000000; i++)
            {
                if (Game(universe))
                {
                    success++;
                    //Console.WriteLine($"Universe {universe} SUCCESS!");
                }
                else
                {
                    failure++;
                    //Console.WriteLine($"Universe {universe} FAILURE!");
                }
                universe++;
                double successRate = (double)success / universe * 100;
                Console.WriteLine($"universes: {universe} successes: {success} failures: {failure}\nSuccess rate is: {successRate}% ");
            }
        }

        private static bool Game(int universe)
        {
            List<int> oth = GenerateOneToHundred();
            Dictionary<int, int> dict = GenerateDictionary(oth);
            for (int prisoner = 1;prisoner < 101;prisoner++)
            {
                if (!Check(prisoner, dict))
                {
                    return false;
                }
            }
            return true;
        }

        private static List<int> GenerateOneToHundred()
        {
            List<int> oth = new List<int>();
            for (int i = 1;i <101; i++)
            {
                oth.Add(i);
            }
            return oth;
        }
        private static Dictionary<int, int> GenerateDictionary(List<int> oth)
        {
            Random rand = new Random();
            Dictionary<int, int> dict = new Dictionary<int, int>();
            for (int i = 1; i <101; i++)
            {
                int x = rand.Next(0, oth.Count);
                dict[i] = oth[x];
                oth.RemoveAt(x);
            }
            return dict;
        }

        private static bool Check(int prisoner, Dictionary<int, int> dict)
        {
            int checking = prisoner;
            for (int i = 0; i < 50; i++)
            {
                //Console.WriteLine($"prisoner {prisoner} is checking box {checking}...");
                int result = dict[checking];
                //Console.WriteLine($"found{result}");
                if (result == prisoner)
                {
                    //Console.WriteLine($"prisoner {prisoner} has found its new host!");
                    return true;
                }
                checking = result;
            }
            //Console.WriteLine("le epic fail!");
            return false;
        }
    }
}