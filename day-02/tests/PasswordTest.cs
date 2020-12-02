using System;
using Xunit;
using day_02;

namespace day_02.test 
{
    public class PasswordTest
    {

        // First we can test V1
        [Fact]
        public void V1GivenStringInputThatMatchesMinimumReturnsTrue()
        {
            var password = new Password("1-3 a: abcde");

            Assert.True(password.ValidatorV1());
        }

        [Fact]
        public void V1GivenStringInputThatMatchesMaximumReturnsTrue()
        {
            var password = new Password("1-3 a: abacdae");

            Assert.True(password.ValidatorV1());
        }

        [Fact]
        public void V1GivenStringInputThatMatchesReturnsTrue()
        {
            var password = new Password("1-3 a: abcdae");

            Assert.True(password.ValidatorV1());
        }

        [Fact]
        public void V1GivenStringInputThatMatchesTooFewReturnsFalse()
        {
            var password = new Password("2-3 a: abcde");

            Assert.False(password.ValidatorV1());
        }

        [Fact]
        public void V1GivenStringInputThatMatchesTooManyReturnsFalse()
        {
            var password = new Password("1-2 a: abcdaae");

            Assert.False(password.ValidatorV1());
        }

        [Fact]
        public void V1GivenStringInputThatMatchesNoneReturnsFalse()
        {
            var password = new Password("2-3 a: bcde");

            Assert.False(password.ValidatorV1());
        }

        // Now test V2
        [Fact]
        public void V2GivenStringInputThatMatchesFirstPositionOnlyReturnsTrue()
        {
            var password = new Password("1-3 a: abcde");

            Assert.True(password.ValidatorV2());
        }

        [Fact]
        public void V2GivenStringInputThatMatchesSecondPositionOnlyReturnsTrue()
        {
            var password = new Password("1-3 a: ebacdae");

            Assert.True(password.ValidatorV2());
        }

        [Fact]
        public void V2GivenStringInputThatMatchesNeitherReturnsFalse()
        {
            var password = new Password("1-3 a: ebcde");

            Assert.False(password.ValidatorV2());
        }

        [Fact]
        public void V2GivenStringInputThatMatchesBothReturnsFalse()
        {
            var password = new Password("1-2 a: aacdaae");

            Assert.False(password.ValidatorV2());
        }
    }
}