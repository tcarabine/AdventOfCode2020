using System;
using Xunit;
using day_02;

namespace day_02.test 
{
    public class ValidatorV2Test
    {
        [Fact]
        public void GivenStringInputThatMatchesFirstPositionOnlyReturnsTrue()
        {
            var input = "1-3 a: abcde";

            Assert.True(Program.PasswordValidatorV2(input));
        }

        [Fact]
        public void GivenStringInputThatMatchesSecondPositionOnlyReturnsTrue()
        {
            var input = "1-3 a: ebacdae";

            Assert.True(Program.PasswordValidatorV2(input));
        }

        [Fact]
        public void GivenStringInputThatMatchesNeitherReturnsFalse()
        {
            var input = "1-3 a: ebcde";

            Assert.False(Program.PasswordValidatorV2(input));
        }

        [Fact]
        public void GivenStringInputThatMatchesBothReturnsFalse()
        {
            var input = "1-2 a: aacdaae";

            Assert.False(Program.PasswordValidatorV2(input));
        }
    }
}