using System;
using Xunit;
using day_02;

namespace day_02.test 
{
    public class ValidatorV1Test
    {
        [Fact]
        public void GivenStringInputThatMatchesMinimumReturnsTrue()
        {
            var input = "1-3 a: abcde";

            Assert.True(Program.PasswordValidatorV1(input));
        }

        [Fact]
        public void GivenStringInputThatMatchesMaximumReturnsTrue()
        {
            var input = "1-3 a: abacdae";

            Assert.True(Program.PasswordValidatorV1(input));
        }

        [Fact]
        public void GivenStringInputThatMatchesReturnsTrue()
        {
            var input = "1-3 a: abcdae";

            Assert.True(Program.PasswordValidatorV1(input));
        }

        [Fact]
        public void GivenStringInputThatMatchesTooFewReturnsFalse()
        {
            var input = "2-3 a: abcde";

            Assert.False(Program.PasswordValidatorV1(input));
        }

        [Fact]
        public void GivenStringInputThatMatchesTooManyReturnsFalse()
        {
            var input = "1-2 a: abcdaae";

            Assert.False(Program.PasswordValidatorV1(input));
        }

        [Fact]
        public void GivenStringInputThatMatchesNoneReturnsFalse()
        {
            var input = "2-3 a: bcde";

            Assert.False(Program.PasswordValidatorV1(input));
        }
    }
}