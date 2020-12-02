using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace day_02
{
    public class Password
    {
        private readonly int _val1, _val2;
        private readonly char _required;
        private readonly string _secret;

        public Password(string input)
        {
            var regex = new Regex(@"(\d+)-(\d+)\s([a-z]):\s(\w+)");
            var match = regex.Match(input);

            _val1 = Convert.ToInt32(match.Groups[1].Value);
            _val2 = Convert.ToInt32(match.Groups[2].Value);
            _required = Convert.ToChar(match.Groups[3].Value);
            _secret = match.Groups[4].Value;
        }

        public bool ValidatorV1()
        {
            var secret = new List<char>(_secret);
            var count = secret.Count(c => c == _required);

            return _val1 <= count && _val2 >= count;
        }

        public bool ValidatorV2()
        {
            var secret = _secret.ToCharArray();
            return (secret[_val1 - 1] == _required || secret[_val2 - 1] == _required) && secret[_val1 - 1] != _secret[_val2 - 1];
        }

    }

    public class Program
    {
        static void Main(string[] args)
        {
            var fileName = "input.txt";
            var passwords = File.ReadAllLines(fileName).ToList().Select(p => new Password(p));

            var test1 = passwords.Count(p => p.ValidatorV1());
            Console.WriteLine($"{test1} Passwords are valid for V1");

            var test2 = passwords.Count(p => p.ValidatorV2());
            Console.WriteLine($"{test2} Passwords are valid for V2");
        }
    }
}
