// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BurnMechanism {
    ERC20 public token;

    constructor(ERC20 _token) {
        token = _token;
    }

    function burn(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        token.transferFrom(msg.sender, address(0), amount);
    }
}
