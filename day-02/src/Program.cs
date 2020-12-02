using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace day_02
{
    public class Program
    {
        static void Main(string[] args)
        {
            var fileName = "input.txt";
            var input = new List<string>();

            input = File.ReadAllLines(fileName).ToList();

            var test1 = input.Count(line => PasswordValidatorV1(line));

            Console.WriteLine($"{test1} Passwords are valid for V1");

            var test2 = input.Count(line => PasswordValidatorV2(line));
            Console.WriteLine($"{test2} Passwords are valid for V1");

        }

        static public bool PasswordValidatorV1(string input)
        {
            var regex = new Regex(@"(\d+)-(\d+)\s([a-z]):\s(\w+)");
            var match = regex.Match(input);
            
            var min = Convert.ToInt32(match.Groups[1].Value);
            var max = Convert.ToInt32(match.Groups[2].Value);
            var required = Convert.ToChar(match.Groups[3].Value);
            var secret = new List<char>();
            secret.AddRange(match.Groups[4].Value);

            var count = secret.Count(c => c == required);

            if ( min <= count && max >= count ) 
            {
                return true;
            } else {
                return false;
            }
        }

        static public bool PasswordValidatorV2(string input)
        {
            var regex = new Regex(@"(\d+)-(\d+)\s([a-z]):\s(\w+)");
            var match = regex.Match(input);
            
            var pos1 = Convert.ToInt32(match.Groups[1].Value);
            var pos2 = Convert.ToInt32(match.Groups[2].Value);
            var required = Convert.ToChar(match.Groups[3].Value);
            var secret = match.Groups[4].Value.ToCharArray();

            if ( 
                (secret[pos1 - 1] == required && secret[pos2 - 1] != required)
                ||
                (secret[pos1 - 1] != required && secret[pos2 - 1] == required) 
            ) 
            {
                return true;
            } else {
                return false;
            }
        }
    }
}
