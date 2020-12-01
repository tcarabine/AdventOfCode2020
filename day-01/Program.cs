using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace day_01
{
    class Program
    {   
        static void Main(string[] args)
        {
            var fileName = "input.txt";
            var target = 2020;
            var input = new List<int>();

            var file = File.ReadAllLines(fileName);
            foreach (var line in file) {
                input.Add(Convert.ToInt32(line));
            }

            foreach (var num in input) {
                var companion = target - num;
                

                if(input.Contains(companion)) {
                    Console.WriteLine($"RESULT {num} * {companion} = {num * companion}");
                    break;
                } else {
                    Console.WriteLine($"NOT {num}");
                }
            }
            

            Console.WriteLine("====== Starting part 2 =======");

            var initialTargets = input.Select( i => target - i);

            foreach (var initialTarget in initialTargets) {
                
                foreach (var num in input) {
                    var companion = initialTarget - num;

                    if(input.Contains(companion)) {
                        var it = target - initialTarget;
                        Console.WriteLine($"RESULT {num} + {companion} + {it} = {num + companion + it}");
                        Console.WriteLine($"RESULT {num} * {companion} * {it} = {num * companion * it}");
                        break;
                    }
                }
            }

        }
    }
}
