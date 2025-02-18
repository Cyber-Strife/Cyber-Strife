// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Governance {
    address public owner;
    uint256 public proposalId;
    mapping(uint256 => Proposal) public proposals;

    struct Proposal {
        string description;
        bool executed;
        uint256 votesFor;
        uint256 votesAgainst;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function createProposal(string memory description) public onlyOwner returns (uint256) {
        proposalId++;
        proposals[proposalId] = Proposal(description, false, 0, 0);
        return proposalId;
    }

    function vote(uint256 id, bool support) public {
        Proposal storage proposal = proposals[id];
        require(!proposal.executed, "Proposal already executed");

        if (support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }
    }

    function executeProposal(uint256 id) public onlyOwner {
        Proposal storage proposal = proposals[id];
        require(!proposal.executed, "Proposal already executed");

        if (proposal.votesFor > proposal.votesAgainst) {
            proposal.executed = true;
        }
    }
}
